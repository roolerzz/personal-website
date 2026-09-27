---
title: "Research"
layout: "single"
hideAuthor: true
---

My work focuses on **storage systems for AI/ML workloads**, bridging production systems experience with storage research:

**Storage Benchmarking & Characterization**
Current GPU training benchmarks (MLPerf Storage, DLIO) focus on throughput but miss critical production behaviors: checkpoint I/O burstiness, metadata operation scalability, and S3 API compatibility edge cases. I'm developing evaluation methodologies that capture these real-world dimensions, informed by production deployments at Crusoe.

**RDMA Object Storage & Accelerated I/O**
Exploring RDMA-based object storage architectures (S3/RDMA) and tier-0 caching systems that reduce checkpoint latency for GPU training. 

**Storage Evaluation Frameworks**
Developing framework for evaluating object storage systems beyond throughput: S3 compatibility testing, failure mode analysis, operational complexity metrics, and total cost of ownership.  Investigating trade-offs between file systems (Lustre, DAOS, 3FS) and emerging disaggregated object storage vendors.

---

### Current Work

Evaluating object storage vendors for GPU training clusters at Crusoe. Member of MLCommons Storage Working Groups (Object Storage, Accelerated IO) and currently looking to contribute to SNIA's Technical Working Groups (Cloud Object Storage Test Tools Group, Accelerated IO).

**Looking to collaborate on the following:**
- Storage Performance Characterization for AI Training Workloads
- Framework for Evaluating Object Storage vendors for AI Workloads

---

## Readings

I am capturing the Research Papers that have helped me learn I will also be capturing my reading notes [here](/notes/).

### AI Storage & ML Infrastructure

**[3FS (Fire-Flyer File System)](https://github.com/deepseek-ai/3FS)** | DeepSeek's RDMA-based Distributed File System

**[Fire-Flyer AI-HPC](https://arxiv.org/html/2408.14158v1)** | Cost-Effective Software-Hardware Co-Design

**[RDMA-First Object Storage with SmartNIC Offload](https://arxiv.org/html/2509.13997v1)** | Low-latency GPU storage

**[DAOS](https://dl.acm.org/doi/10.1007/978-3-030-48842-0_3)** | Storage Stack for Storage Class Memory

**[Benchmarking All-Flash Storage for HPC](https://pdsw.org/pdsw21/papers/ws_pdsw_paper_S2_P1_paper-lockwood.pdf)** | Storage benchmarking methodologies

**[io_uring for High-Performance DBMSs](https://arxiv.org/pdf/2512.04859v1)** | Modern Linux async I/O

---

### Distributed Storage & Databases

**[Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)** | Amazon's Highly Available Key-Value Store (SOSP 2007)
[My Notes](/notes/dynamo-2007/)

**[DynamoDB](https://www.usenix.org/conference/atc22/presentation/elhemali)** | Amazon's Fully Managed NoSQL Service
[My Notes](/notes/dynamodb-2022/)

**[Spanner](https://storage.googleapis.com/gweb-research2023-media/pubtools/1974.pdf)** | Google's Globally-Distributed Database
[My Notes](/notes/spanner-2012/)

**[Cassandra](https://research.cs.cornell.edu/ladis2009/papers/lakshman-ladis2009.pdf)** | Distributed Wide-Column Store
[My Notes](/notes/cassandra-2009/)

**[Bigtable](https://storage.googleapis.com/gweb-research2023-media/pubtools/4443.pdf)** | Distributed Storage for Structured Data
[My Notes](/notes/bigtable-2006/)

**[Megastore](https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf)** | Scalable, Highly Available Storage
[My Notes](/notes/megastore-2011/)

---

### Distributed File Systems

**[Google File System](https://storage.googleapis.com/gweb-research2023-media/pubtools/4446.pdf)** | Large-scale distributed file system
[My Notes](/notes/gfs-2003/)

**[HDFS](https://pages.cs.wisc.edu/~akella/CS838/F15/838-CloudPapers/hdfs.pdf)** | Hadoop Distributed File System
[My Notes](/notes/hdfs-2010/)

---

### Consensus & Coordination

**[Raft](https://raft.github.io/)** | Consensus Algorithm
[My Notes](/notes/raft-2014/)

**[Chubby](https://storage.googleapis.com/gweb-research2023-media/pubtools/4444.pdf)** | Distributed Lock Service
[My Notes](/notes/chubby-2006/)

**[Paxos Made Live](https://dl.acm.org/doi/10.1145/1281100.1281103)** | Consensus

**[Time, Clocks, and Ordering](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)** | Lamport's Classic

---

### Streaming & Messaging

**[Kafka](https://notes.stephenholiday.com/Kafka.pdf)** | Distributed Append-Only Log
[My Notes](/notes/kafka-2011/)

**[MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)** | Simplified Data Processing

**[Spark](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)** | Resilient Distributed Datasets

**[Flink](https://asterios.katsifodimos.com/assets/publications/flink-deb.pdf)** | Stream and Batch Processing

---

### Caching & Performance

**[Memcache at Facebook](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf)** | Scaling Memcache
[My Notes](/notes/memcache-2012/)

**[TAO](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)** | Facebook's Distributed Data Store

---

### Books

**[Designing Data-Intensive Applications](https://dataintensive.net/)** by Martin Kleppmann

**[Database Internals](https://www.databass.dev/)** by Alex Petrov

**[A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php)** by John Ousterhout
