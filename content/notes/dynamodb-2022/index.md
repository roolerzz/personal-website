---
title: "Whitepaper: DynamoDB - Amazon's highly available Database"
date: 2025-12-27
draft: false
tags: ["distributed-systems", "nosql", "aws", "dynamodb", "paper-notes"]
categories: ["paper-notes"]
ShowToc: true
TocOpen: true
weight: 1
---

**Paper:** [Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL Database Service](https://www.usenix.org/conference/atc22/presentation/elhemali) (USENIX ATC 2022)

---

## Reading Notes

### Introduction & Background

- DDB is a NoSQL cloud DB service providing consistent single-digit millisecond perf at any scale
- Handles 89.2M requests/sec during 66-hour Prime Day 2021
- 99.99% availability for regular tables, 99.999% for global tables
- Design goal: complete all requests with low single-digit millisecond latencies

**[Context]** DDB evolved from Dynamo (2007 paper)
- Dynamo created for shopping cart (needed high scalability, availability, durability for key-value)
- Dynamo limitation: operational complexity (single-tenant, teams had to manage their own installations)
- SimpleDB limitation: 10GB capacity limit, unpredictable latencies, all attributes indexed

**DDB solution combined:**
- From Dynamo: incremental scalability, predictable high perf
- From SimpleDB: ease of admin, consistency, table-based data model

### Six Fundamental Properties

1. **Fully managed cloud service**
   - No patching, hardware mgmt, cluster config
   - Handles provisioning, recovery, encryption, upgrades, backups

2. **Multi-tenant architecture**
   - Different customer data on same physical machines
   - Resource reservations + tight provisioning + monitored usage = isolation

3. **Boundless scale**
   - No predefined limits on data amount
   - Scales from several servers to thousands

4. **Predictable performance**
   - GetItem/PutItem in same AWS region: low single-digit ms latencies for 1KB item
   - Consistent regardless of table size or request volume

5. **High availability**
   - Replicates across multiple AZs
   - Auto re-replication on disk/node failure
   - Global tables: geo-replicated for DR and low latency
   - SLA: 99.99% regular, 99.999% global tables

6. **Flexible use cases**
   - Supports both strong consistency and eventual consistency
   - Flexible schema

### Architecture Overview

**Data model:**
- Table = collection of items
- Item = collection of attributes
- Primary key: simple (partition key only) or composite (partition key + sort key)
- Partition key hashed to determine storage location
- Secondary indexes for alternate query patterns

**Core CRUD operations:**

| Operation | Description |
|-----------|-------------|
| `PutItem` | Insert new or replace old item |
| `UpdateItem` | Update existing or add new if doesn't exist |
| `DeleteItem` | Delete single item by primary key |
| `GetItem` | Return attributes for item with given primary key |

- Also supports ACID transactions: `TransactWriteItems`, `TransactGetItems`

**Partitioning and replication:**
- Table divided into multiple partitions
- Each partition: disjoint and contiguous part of table's key-range
- Each partition has multiple replicas across different AZs
- Uses Multi-Paxos for leader election and consensus
- Replica can trigger election, elected leader maintains leadership via lease renewal

**Storage replica types:**

![Storage Node Architecture](storage-node.png)

1. **Storage Node (full replica)**
   - B-Tree (key-value data) + WAL
   - Stores actual data

2. **Log Replica (lightweight replica)**
   - WAL only
   - Fast healing when storage replica fails (seconds vs. minutes)

**[Important]** Leader responsibilities:
- Only leader serves writes and strongly consistent reads
- Leader generates WAL record, sends to peers
- Write acked once quorum of peers persists log record

**Read types:**
- Strong consistency: read from leader
- Eventual consistency: read from any replica

**[Catch]** Failure handling:
- If leader fails, peer can propose new election
- New leader won't serve writes/consistent reads until old leader's lease expires
- Upon detecting unhealthy storage replica, leader adds log replica (fast healing)

### Microservice Architecture

![DynamoDB Architecture](dynamodb-architecture.png)

DDB uses microservice architecture:

**1. Metadata Service**
- Stores routing info about tables, indexes, replication groups
- Provides mapping from keys to storage nodes

**2. Request Router Service**
- Authentication: verifies request authenticity
- Authorization: checks permissions
- Routing: looks up routing info from Metadata Service, forwards to storage node

**3. Storage Service**
- Stores customer data on fleet of storage nodes
- Manages B-Trees and WALs
- Handles replication via Paxos

**4. Auto-Admin Service** (Central Nervous System of DDB)
- Resource creation, updates, DDL
- Fleet health monitoring
- Partition health monitoring
- Scaling of tables
- Control plane request execution
- **Critical:** monitors health of all partitions + core components, replaces unhealthy replicas/hardware

**5. Additional Feature Services**
- Point-in-Time Restore (35 days)
- On-Demand Backups (S3)
- Update Streams (change data capture)
- Global Admission Control
- Global Tables (multi-region)
- Global Secondary Indexes
- Transactions

### The Provisioned Throughput Journey

**Initial design:**
- Customers specified throughput as RCUs (Read Capacity Units) and WCUs (Write Capacity Units)
- Called "provisioned throughput"
- Partition abstraction for dynamic scaling
- As table demands changed, partitions could split and migrate

**[Problem]** Tightly coupled capacity and performance to individual partitions:

1. **Hot partitions**
   - Non-uniform access patterns caused certain partitions to get disproportionate traffic
   - Hot items could belong to stable set of partitions or hop around

2. **Throughput dilution**
   - When partitions split for size, allocated throughput divided equally
   - Per-partition throughput decreased after split
   - Hot partition could have LESS capacity after split

**Admission control architecture:**
- Ensures storage nodes don't become overloaded
- Provides isolation between co-resident table partitions
- Enforces throughput limits
- Admission control was shared responsibility of all storage nodes for a table
- Storage nodes independently performed admission control based on local partition allocations

**Capacity allocation:**
- Allocated throughput of each partition used to isolate workloads
- DDB enforced cap on max throughput per partition
- Total throughput of all partitions on node <= max allowed throughput of node
- Throughput adjusted when table's overall throughput changed or partitions split

**Example scenario:**
```
Max partition throughput = 1000 WCUs

Table created with 3200 WCUs → 4 partitions, each 800 WCUs
Table increased to 3600 WCUs → Each partition: 900 WCUs
Table increased to 6000 WCUs → Split to 8 partitions, each 750 WCUs
Table decreased to 5000 WCUs → Each partition: 625 WCUs
```

**[Wrong assumptions]**
1. Applications uniformly access keys in table
2. Splitting partition for size equally splits performance

**Reality:** Non-uniform access patterns both over time and over key ranges. Splitting hot partition could worsen problem.

**Common challenges:**
- Traffic going to few items
- Throttling occurred even when table's total provisioned throughput sufficient
- Customers would increase provisioned throughput even when under overall limit
- Poor performance despite adequate capacity

**[Root cause]** Tightly coupling rigid performance allocation to each partition and dividing that allocation as partitions split

### Improvements to Admission Control

**Key observations:**
1. Partitions had non-uniform access/traffic
2. Not all partitions hosted by storage node used allocated throughput simultaneously

**Innovation 1: Bursting**

**[Concept]** Let apps tap into unused capacity at partition level on best-effort basis to absorb short-lived spikes

**Mechanism:**
- DDB retained portion of partition's unused capacity for later bursts (up to 300 seconds)
- Unused capacity = "burst capacity"
- Utilized when consumed capacity exceeded provisioned capacity of partition
- Still maintained workload isolation (partition could only burst if unused throughput existed at node level)

**Token bucket implementation:**
- Multiple token buckets for admission control
- Two for each partition: Allocated tokens + Burst tokens
- One for storage node

**Request handling:**

Using allocated capacity:
```
[Partition Allocated Tokens] + [Node Tokens] available
→ Request admitted
→ Deduct from both buckets
```

Using burst capacity:
```
[Partition Allocated Tokens] exhausted
[Partition Burst Tokens] + [Node Tokens] available
→ Request admitted via bursting
→ Deduct from burst + node buckets
```

**Read vs. Write handling:**
- Read requests: accepted based on local token buckets
- Write requests using burst: require additional check on node-level token bucket of other replica members
- Leader replica periodically collected info about each member's node-level capacity

**[Impact]** Helped absorb short-lived spikes, significantly improved experience for bursty workloads (best-effort, dependent on node having available throughput)

**Innovation 2: Adaptive Capacity**

**[Goal]** Better absorb long-lived spikes that can't be absorbed by burst capacity alone

**Mechanism:**
- Actively monitored provisioned and consumed capacity of all tables
- Automatic boost: if table experienced throttling AND table-level throughput not exceeded, automatically increased allocated throughput of affected partitions
- Used proportional control algorithm to adjust allocations
- If table consumed more than provisioned capacity, boosted partitions had capacity decreased

**Operational support:**
- Autoadmin ensured boosted partitions relocated to nodes with capacity to serve increased throughput

**[Characteristics]** Best-effort, reactive (kicked in only after throttling observed)

**[Impact]** Eliminated over 99.99% of throttling due to skewed access patterns

**Limitations of bursting and adaptive capacity:**
- Bursting: only helpful for short-lived spikes, dependent on node having throughput
- Adaptive capacity: reactive (not proactive), kicked in only after throttling

**[Key takeaway]** Fundamental issue was tightly coupling partition-level capacity to admission control. Admission control was distributed and performed at partition level.

### Global Admission Control (GAC)

**[Breakthrough]** Realized it would be beneficial to:
1. Remove admission control from partition
2. Let partition always burst (no static allocation)
3. Provide workload isolation centrally

**Core concept:**
- GAC service centrally tracks total consumption of table capacity in terms of tokens
- Each request router maintains local token bucket for admission decisions
- Request routers communicate with GAC to replenish tokens at regular intervals (few seconds)

**Key design properties:**
1. Each GAC server can be stopped/restarted without impacting service operation
2. Each GAC server can track one or more token buckets (configured independently)
3. All GAC servers part of independent hash ring (redundancy + scaling)

**Request flow:**

Token management by request routers:

1. **Local token consumption:**
   - Request router manages several time-limited tokens locally
   - When app request arrives, router deducts tokens
   - Eventually runs out due to consumption or expiry

2. **Token replenishment:**
   - When router runs out of tokens, requests more from GAC
   - GAC uses info provided by client to:
     - Estimate global token consumption
     - Vend tokens available for next time unit to client's share of overall tokens

3. **Global fairness:**
   - Ensures non-uniform workloads sending traffic to only subset of items can execute up to max partition capacity
   - No longer limited by static partition allocation

**Defense in depth:**
- Partition-level token buckets retained in addition to GAC
- Capacity of these buckets capped
- Purpose: ensure one app doesn't consume all/significant share of resources on storage nodes
- Provides additional layer of protection

**[Result]** GAC provides global fairness + handling of non-uniform workloads. Partition-level caps provide resource isolation + protection.

### Balancing Consumed Capacity

**[Challenge]** Letting partitions always burst required DDB to manage burst capacity effectively

**Context:**
- Multiple partitions from various tables with different traffic patterns
- Heterogeneous hardware fleet
- Need allocation scheme deciding which replicas can safely co-exist
- Must not violate: availability, predictable performance, security, elasticity

**Previous approach (provisioned tables without bursting):**
- Static partition allocations
- Partitions never allowed to take more traffic than allocated capacity
- No noisy neighbors
- Simple: find storage nodes that could accommodate partition based on allocated capacity

**New problem with bursting:**
- Partitions reacting to changing workload could cause storage node to exceed prescribed capacity
- System could pack storage nodes with partition replicas whose total capacity (including burst) exceeded node's overall capacity
- Risk of overloading nodes and impacting availability

**[Solution]** Proactive balancing:
- Implemented system to proactively balance partitions across storage nodes based on:
  - Throughput consumption
  - Storage size

**Mechanism:**
1. Each storage node independently monitors overall throughput and data size of all hosted replicas
2. When throughput exceeds threshold % of node's max capacity, node reports to autoadmin
3. Report includes list of candidate partition replicas to move from current node
4. Autoadmin orchestrates partition movement to balance load

**Benefits:** mitigates availability risks from tightly packed replicas, maintains performance predictability, enables safe bursting

### Splitting for Consumption

**[Problem]** Even with GAC and ability for partitions to always burst, tables could still experience throttling if traffic skewed to specific set of items within partition

**[Solution]** Consumption-based splitting

**Trigger:** DDB automatically scales out partitions once consumed throughput crosses certain threshold

**Split point selection:**
- Split point in key range chosen based on observed key distribution
- Observed key distribution serves as proxy for app's access pattern
- More effective than splitting key range in middle

**Timeline:** partition splits usually complete in order of minutes

**[Limitations]** Workloads that can't benefit:
1. Single hot item: partition receiving high traffic to single item can't be split effectively
2. Sequential access: partition where key range accessed sequentially won't benefit from split

**Response:** DDB avoids splitting partition (recognizes futility)

### On-Demand Provisioning

**Context:**
- Apps migrating to DDB came from self-provisioned servers
- DDB introduced new provisioning model: RCUs and WCUs

**Customer challenges:**
1. Concept of capacity units was new
2. Difficult to forecast provisioned throughput
3. Two common outcomes:
   - Over-provisioning: low utilization, wasted money
   - Under-provisioning: throttling, poor performance

**[Solution]** On-demand tables: remove burden of figuring out right provisioning

**How it works:**
1. DDB provisions on-demand tables based on consumed capacity
2. Collects signals of reads and writes
3. Instantly accommodates up to double the previous peak traffic on table
4. Scales table by splitting partitions for consumption
5. Split decision algorithm based on traffic patterns

**Benefits:**
- No capacity planning
- Automatically scales with workload
- Pay only for what you use
- Ideal for unpredictable or spiky workloads

**GAC integration:** GAC allows DDB to monitor and protect system from one app consuming all resources. Even with on-demand, GAC provides global fairness and resource protection.

### Durability and Correctness

Data loss can occur due to hardware failures, software bugs, hardware bugs. DDB designed for high durability through mechanisms to prevent, detect, and correct potential data losses.

**Hardware failures:**

Write-Ahead Logs (WAL):
- Central for durability and crash recovery
- Stored in all three replicas of partition
- For higher durability, WAL periodically archived to S3
- S3 designed for 11 nines (99.999999999%) durability
- Unarchived logs typically few hundred MB

**Fast healing with log replicas:**

**[Problem]** When storage node fails, all replication groups on node down to two copies. Healing storage replica takes several minutes (must copy B-tree + WAL). During healing window, durability at risk.

**[Solution]** Upon detecting unhealthy storage replica, leader adds log replica. Adding log replica takes only few seconds (copy only recent WAL, not B-tree). Ensures high durability of most recent writes. Quick restoration of three-way replication.

**Silent data errors:**

**[Problem]** Some hardware failures cause incorrect data to be stored. Can occur in storage media, CPU, or memory. Very difficult to detect. Can happen anywhere in system.

**[Solution]** Extensive use of checksums

Checksum locations:
- Every log entry: validates data integrity
- Every message: protects inter-node communication
- Every log file: ensures storage integrity

Data transfer validation:
- DDB validates data integrity for every data transfer between two nodes
- Checksums serve as guardrails to prevent errors from spreading

**Log archival process:**

Agent responsible for archiving log files to S3 performs checks:
1. Verification of log entries: ensure each entry belongs to correct table and partition
2. Checksum verification: detect any silent errors
3. Hole detection: verify log file has no gaps in sequence numbers

After passing checks:
- Log file and manifest archived to S3
- Manifest contains: table, partition, start/end markers for data in log file

Multi-replica verification:
- Log archival agents run on all three replicas of replication group
- If agent finds log file already archived, it:
  1. Downloads uploaded file
  2. Verifies integrity by comparing with local WAL
  3. Ensures consistency across replicas

S3 upload protection:
- Every log file and manifest uploaded with content checksum
- S3 checks content checksum during PUT operation
- Guards against errors during data transit to S3

**Continuous verification:**

**[Goal]** Detect any silent data errors or bit rot in system

Scrub process:
- Purpose: detect errors not anticipated, such as bit rot
- Verifies:
  1. All three copies of replicas in replication group have same data
  2. Data of live replicas matches copy of replica built offline using archived WAL entries
- Verification method: computes checksum of live replica, matches with snapshot generated from log entries archived in S3
- Acts as defense in depth to detect divergences
- Verifies live storage replicas against replicas built using history of logs from inception of table
- Similar technique used to verify replicas of global tables

**[Key lesson]** "Continuous verification of data-at-rest is the most reliable method of protecting against hardware failures, silent data corruption, and even software bugs."

### Software Bugs

**[Problem]** DDB is complex distributed key-value store. High complexity increases probability of human error in design, code, operations. Potential consequences: loss/corruption of data, violation of interface contracts.

**[Solution]** Formal methods

TLA+ specification:
- Core replication protocol specified using TLA+ (formal specification language)
- When new features affect replication protocol:
  1. Incorporated into TLA+ specification
  2. Model checked for correctness

**Impact:** model checking caught subtle bugs that could have led to durability and correctness issues. Bugs caught before code went into production. Similar approach used by S3.

Scope of formal methods:
- Data plane: replication protocol verification
- Control plane: correctness verification
- Features: distributed transactions verification

**Beyond formal methods:**
- Extensive failure injection testing
- Stress testing
- Ensures correctness of every piece of software deployed

### Backups and Restore

**Purpose:** protect against logical corruption due to bug in customer's app, accidental data deletion, app errors

**On-demand backups:**
- Built using WALs archived in S3
- No impact on performance or availability of table
- Consistent across multiple partitions up to nearest second
- Full copies of DDB tables
- Stored in S3 bucket

**Point-in-Time Restore (PITR):**
- Restore contents of table that existed at any time in previous 35 days
- Restore to different DDB table in same region

How it works (for tables with PITR enabled):
1. DDB creates periodic snapshots of partitions (frequency based on amount of WAL accumulated)
2. Snapshots uploaded to S3
3. Snapshots used in conjunction with WAL for restore

Restore workflow:
1. User requests PITR for table at specific timestamp
2. DDB identifies closest snapshots to requested time for all partitions
3. Applies logs up to timestamp in restore request
4. Creates snapshot of restored table
5. Restores to new table

**Advantages:** granularity (restore to any second in 35-day window), flexibility (restore to new table, original remains unchanged), no performance impact (built from S3-archived data)

### Availability

**High-level goals:**
- SLA: 99.99% (4 nines) for regional tables, 99.999% (5 nines) for global tables
- Regular testing of resilience to node, rack, AZ failures
- Power-off tests with realistic simulated traffic
- Verification that data remains logically valid and uncorrupted

**Write and consistent read availability:**

Dependencies:
- Partition's write availability depends on:
  1. Healthy leader
  2. Healthy write quorum

Write quorum in DDB:
- Consists of two out of three replicas from different AZs
- Multi-Paxos consensus required for writes

Partition availability:
- Remains available as long as write quorum can be achieved (2 of 3 replicas) and leader exists
- If minimum replicas for quorum unavailable, partition becomes unavailable for writes

Fast healing with log replicas:
- If one replica unresponsive, leader adds log replica to group
- Fastest way to ensure write quorum always met
- Takes seconds instead of minutes

Read availability:
- Consistent reads: served by leader replica only
- Eventually consistent reads: can be served by any replica

Leader failure:
- Other replicas detect failure, elect new leader
- Minimizes disruptions to consistent read availability
- New leader waits for old leader's lease to expire before serving writes/consistent reads

**[Impact of formal methods]** Formally proven Paxos implementation gave confidence to experiment with log replicas. Enabled running millions of Paxos groups in Region with log replicas.

**Failure detection:**

**[Challenge]** Newly elected leader must wait for expiry of old leader's lease before serving traffic. Takes couple seconds. During this period: no new writes or consistent reads. Disrupts availability.

**Requirements:**
- Failure detection must be quick to minimize disruptions
- Failure detection must be robust to avoid false positives
- False positives lead to unnecessary failovers and more disruptions

Standard failure detection:
- Works well when every replica of group loses connection to leader
- Example: network partition, leader node failure

**Gray failures:**

**[Definition]** Network failures that are not complete but cause partial connectivity issues:
- Communication issues between leader and follower
- Issues with outbound or inbound communication of node
- Front-end routers facing issues communicating with leader (even though leader and followers can communicate)

Impact of gray failures:
- Can disrupt availability due to:
  - False positives in failure detection
  - No failure detection (when it should have been detected)

Example scenario:
- Replica not receiving heartbeats from leader tries to elect new leader
- If other replicas can still communicate with leader, this is false positive
- Unnecessary failover disrupts availability

**[Solution]** Improved failure detection algorithm:

Enhanced approach:
1. Follower wanting to trigger failover sends message to other replicas asking: "Can you communicate with the leader?"
2. If replicas respond with "healthy leader" message, follower drops attempt to trigger election
3. This validation step significantly reduces false positives

**[Impact]** Significantly minimized number of false positives in system. Reduced spurious leader elections. Improved overall availability.

**Measuring availability:**

Service and table level monitoring:
- DDB continuously monitors availability at both levels
- Tracks availability data for analysis and alarming

Customer-Facing Alarms (CFA):
- Trigger if customers see errors above certain threshold
- Report availability-related problems
- Enable proactive mitigation (automatic or operator intervention)

Daily aggregation jobs:
- Calculate aggregate availability metrics per customer
- Results uploaded to S3 for regular analysis
- Used for analyzing availability trends

**Client-side availability measurement:**

Two sets of clients measure user-perceived availability:

1. **Internal Amazon services:**
   - Services using DDB as data store
   - Share availability metrics for DDB API calls as observed by their software
   - Provides real production workload data

2. **DDB canaries:**
   - Apps run from every AZ in Region
   - Talk to DDB through every public endpoint
   - Synthetic workload monitoring
   - Catches issues that might not appear in aggregate metrics

**Benefits of real app traffic:** reason about DDB availability and latencies as seen by customers. Catch gray failures that might not be detected by server-side metrics alone. Validates end-to-end availability including network path.

### Deployments

**Challenge:** zero-downtime deployments. Unlike traditional relational DBs, DDB takes care of deployments without need for maintenance windows and without impacting performance and availability.

**Non-atomic deployments:**

**[Problem]** Deployments not atomic in distributed systems. At any given time:
- Some nodes run old code
- Other nodes run new code

Compatibility issues:
- New software might introduce new message types
- Protocol changes might not be understood by old software

**[Solution]** Read-write deployments

Multi-step process:

Step 1: Deploy read capability
- Deploy software that can read new message format or protocol
- All nodes now understand new messages

Step 2: Deploy write capability
- Once all nodes can handle new messages
- Update software to send new messages

**Benefits:** both old and new messages can coexist in system. Even in rollbacks, system understands both message types. Ensures forward and backward compatibility.

**OneBox testing:**
- Deployments done on small set of nodes first before pushing to entire fleet
- Reduces potential impact of faulty deployments
- Allows validation in production environment with limited blast radius

**Automatic rollbacks:**

Alarm-based rollbacks:
- DDB sets alarm thresholds on availability metrics
- If error rates or latency exceed thresholds during deployments:
  - System triggers automatic rollbacks
  - Prevents widespread impact

Monitoring during deployments:
- AlarmWatcher monitors key metrics
- Integrated with approval workflow
- Can automatically abort deployments

**Handling leader failovers during deployments:**

**[Problem]** Software deployments to storage nodes can trigger leader failovers. Could impact availability.

**[Solution]** Graceful leadership handoff:
- Leader replicas relinquish leadership before shutdown
- Group's new leader doesn't have to wait for old leader's lease to expire
- Designed to avoid any impact to availability

**Benefits:** smooth transition during deployments. No waiting for lease expiration. Maintains availability throughout deployment.

**Rollback testing:**

**[Problem]** Rollback procedure often missed in testing. Can lead to customer impact when rollback needed.

DDB approach:
- Runs suite of upgrade and downgrade tests at component level before every deployment
- Software intentionally rolled back and tested
- Functional tests run after rollback
- Ensures rollback path as tested as forward path

### Dependencies on External Services

**High availability principle:** to ensure DDB's high availability, all services in request path should either:
1. Be more highly available than DDB, OR
2. Allow DDB to continue operating even when dependency impaired

**Key dependencies:**
- AWS IAM: authentication and authorization
- AWS KMS: encryption key management for tables using customer keys

**Usage:** DDB uses IAM and KMS to authenticate every customer request. Critical for security but potentially risky for availability.

**[Challenge]** IAM and KMS are highly available but no service has 100% availability. If DDB requires real-time calls to these services for every request:
- IAM or KMS impairment would directly impact DDB availability
- Violates availability goals

**[Solution]** Statically stable design

"Static stability" means overall system keeps working even when dependency becomes impaired.

Characteristics:
- System may not see updated info that dependency was supposed to deliver
- However, everything before dependency became impaired continues to work
- No cascading failure despite impaired dependency

**Implementation: aggressive caching**

For IAM and KMS:
1. DDB caches results from IAM and KMS in request routers
2. Request routers perform authentication of every request using cached data
3. Cache periodically refreshed asynchronously (not on critical path)

If dependency becomes unavailable:
- Routers continue using cached results for predetermined extended period
- Existing authenticated users can continue accessing DDB
- New authentication info can't be updated, but existing access continues

**Benefits:**
1. No real-time dependency: removes IAM/KMS from critical request path
2. Improved latency: no synchronous calls to external services for each request
3. High availability maintained: system continues operating during dependency impairment
4. Security preserved: cached credentials still valid, no security compromise

**Trade-offs:** new policy changes or key rotations may not take effect immediately. Bounded by cache TTL and extended period policy. Acceptable trade-off for availability.

**Design philosophy:** prefer static stability over real-time accuracy when availability critical. Cache aggressively, refresh asynchronously. Allow system to continue operating on slightly stale but valid data during impairments.

### DynamoDB Limits

**Per partition capacity limits:**

Read capacity:
- 3000 RCUs per second per partition
- For items up to 4KB in size
- 1 RCU = 1 strongly consistent read op = 2 eventually consistent read ops

Example (20KB item):
- 1 strongly consistent read = 5 RCUs (20KB / 4KB = 5)
- Max 600 strongly consistent read ops per second on single item in partition (3000 RCUs / 5)

Write capacity:
- 1000 WCUs per second per partition
- For items up to 1KB in size
- 1 WCU = 1 write op

**Query and scan limits:**

1 MB limit:
- Applies to data returned by single Query, Scan, or GetItem operation
- Includes size of all returned items (requested attributes + result attributes)
- If total size exceeds 1 MB:
  - DDB returns partial result
  - Provides `LastEvaluatedKey` for pagination
  - Use `LastEvaluatedKey` in subsequent calls to retrieve remaining data

**Batch operations:**

BatchGetItem:
- Can return up to 16 MB of data per operation
- Can retrieve up to 100 items per request

**Item size limit:**

400 KB maximum:
- Each item stored in table limited to 400 KB
- Includes all attribute names and values

Strategies for larger items:

1. Compression:
   - Use GZIP or LZO compression
   - Store as BINARY type
   - Transparent to app after decompression

2. Offloading to S3:
   - Store large data in S3
   - Keep S3 object reference in DDB
   - **Important:** DDB doesn't support transactions across S3 and DDB
   - App must handle failures and cleanup orphaned S3 objects

**Secondary indexes:**

Global Secondary Indexes (GSI):
- Max 20 GSIs per table
- Can be created/deleted after table creation
- Eventually consistent reads only

Local Secondary Indexes (LSI):
- Max 5 LSIs per table
- Must be created at table creation time
- Can support strongly consistent reads

**Transactions:**

TransactWriteItems:
- Synchronous and idempotent write operation
- Groups up to 100 write actions in single all-or-nothing operation
- Aggregate size of items in transaction can't exceed 4 MB

TransactGetItems:
- Synchronous read operation
- Can read up to 100 items
- Aggregate size can't exceed 4 MB

### Micro-Benchmarks

**Purpose:** demonstrate that scale doesn't affect latencies observed by apps

**YCSB workloads:**

Ran Yahoo! Cloud Serving Benchmark (YCSB) workloads:

Workload A:
- 50% reads
- 50% updates
- Uniform key distribution
- Item size: 900 bytes

Workload B:
- 95% reads
- 5% updates
- Uniform key distribution
- Item size: 900 bytes

**Scale test:**

Throughput scaling:
- Scaled from 100,000 ops/sec to 1,000,000 ops/sec
- 10x increase in throughput

**Results:**

Key finding: read latencies show very little variance. Latencies remain identical even as throughput increases 10x.

| Metric | YCSB-A | YCSB-B |
|--------|--------|--------|
| Read P50 | ~same across all throughput levels | ~same across all throughput levels |
| Read P99 | ~same across all throughput levels | ~same across all throughput levels |
| Write P50 | ~stable | ~stable |
| Write P99 | ~stable | ~stable |

**Conclusion:** micro-benchmarks validate DDB's core design goal: "Complete all requests with low single-digit millisecond latencies." Even at massive scale (1M ops/sec), latency remains predictable and consistent.

---

## Diagrams from Paper

### Log Replica Architecture

![Log Replica Architecture](log-replica.png)

Shows how log replicas provide fast healing:
- Storage nodes contain both B-tree and WAL
- Log replicas contain only WAL
- Adding log replica takes seconds vs. minutes for full storage replica
- Maintains write quorum (2 of 3) for durability

---

## How to Cite This Note

**BibTeX:**
```bibtex
@techreport{sethi2025dynamodb,
  author = {Sethi, Hemant},
  title = {Technical Notes: Amazon DynamoDB (USENIX ATC 2022)},
  year = {2025},
  url = {https://sethihemant.com/notes/dynamodb-2022/},
  note = {Accessed: 2025-12-27}
}
```

**APA:**
```
Sethi, H. (2025). Technical Notes: Amazon DynamoDB (USENIX ATC 2022).
Retrieved from https://sethihemant.com/notes/dynamodb-2022/
```

---

## References

**Original Paper:**
```
Elhemali, M., Gallagher, N., Gordon, N., Idziorek, J., Krog, R., Lazier, C.,
Mo, E., Mritunjai, A., Perianayagam, S., Rath, T., Sivasubramanian, S.,
Sorenson III, J. C., Sosothikul, S., Terry, D., & Vig, A. (2022).
Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Managed NoSQL
Database Service. In 2022 USENIX Annual Technical Conference (USENIX ATC 22)
(pp. 1037-1048).
```

**Paper Link:** https://www.usenix.org/conference/atc22/presentation/elhemali

---

*Last updated: December 27, 2025*

*Questions or discussion? [Email me](mailto:sethi.hemant@gmail.com)*
