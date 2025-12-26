---
title: "Research & Reading"
layout: "single"
hideAuthor: true
---

This page documents notes on papers and books that inform my learning and work building distributed systems and AI storage infrastructure.

---

## Books

- **[Designing Data-Intensive Applications](https://dataintensive.net/)** by Martin Kleppmann
  [📝 My Notes]()

- **[Database Internals](https://www.databass.dev/)** by Alex Petrov
  [📝 My Notes]()

- **[A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php)** by John Ousterhout
  [📝 My Notes]()

---

## Research Papers & Systems

### Distributed Storage & Databases

**[Dynamo:](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)** Amazon's Highly Available Key-Value Store(2007)
[📝 My Notes](/posts/dynamo-paper-notes/) 

**[Cassandra:](https://research.cs.cornell.edu/ladis2009/papers/lakshman-ladis2009.pdf)**  Distributed Wide-Column Store(2009)
[📝 My Notes]()

**[DynamoDB:](https://www.usenix.org/conference/atc22/presentation/elhemali)** Amazon's Fully Managed NoSQL Database Service [📝 My Notes]()

**[Spanner:](https://storage.googleapis.com/gweb-research2023-media/pubtools/1974.pdf)** Google's Globally-Distributed Database(2013)
[📝 My Notes]()


**[Bigtable:](https://storage.googleapis.com/gweb-research2023-media/pubtools/4443.pdf)** A Distributed Storage System for Structured Data(2006)
[📝 My Notes]()

**[Megastore:](https://www.cidrdb.org/cidr2011/Papers/CIDR11_Paper32.pdf)** Providing Scalable, Highly Available Storage(2011)
[📝 My Notes]()

### Distributed Messaging & Streaming

**[Kafka:](https://notes.stephenholiday.com/Kafka.pdf)** Distributed Append-Only Log(2011) [📝 My Notes]()

**[MapReduce:](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)** Simplified Data Processing on Large Clusters (2004) [📝 My Notes]()

**[Spark:](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)** Resilient Distributed Datasets: Fault-Tolerant Abstraction for
In-Memory Cluster Computing (2012) [📝 My Notes]()

**[Flink:](https://asterios.katsifodimos.com/assets/publications/flink-deb.pdf)** Stream and Batch Processing(2015) [📝 My Notes]()

### Distributed Coordination & Consensus

**[Chubby:](https://storage.googleapis.com/gweb-research2023-media/pubtools/4444.pdf)**  Distributed Lock/Coordingation Service(2006) [📝 My Notes]()

**[Paxos Made Live:](https://dl.acm.org/doi/10.1145/1281100.1281103)** (2007) [📝 My Notes]()

**[Raft:](https://raft.github.io/)** Consensus Algorithm(2014) [📝 My Notes]()

**[Time, Clocks, and Lamport Ordering:](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)** (1978) [📝 My Notes]()

### Distributed File Systems

**[Google File System](https://storage.googleapis.com/gweb-research2023-media/pubtools/4446.pdf)** Large-scale distributed file system design(2003) [📝 My Notes]()

**[HDFS:](https://pages.cs.wisc.edu/~akella/CS838/F15/838-CloudPapers/hdfs.pdf)**  Hadoop Distributed File System(2010) [📝 My Notes]()

### Caching & Performance

**[Memcache:](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf)** Scaling Memcache at Facebook(2013) [📝 My Notes]()

**[TAO:](https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf)** Facebook's Distributed Data Store(2013) [📝 My Notes]()

### Infrastructure & Networking

**[Zuul:](https://github.com/Netflix/zuul)** Async non-blocking gateway architecture  • [Netflix's Gateway Service](https://netflixtechblog.com/zuul-2-the-netflix-journey-to-asynchronous-non-blocking-systems-45947377fb5c) • [Video](youtube.com/watch?v=6w6E_B55p0E&ab_channel=InfoQ)

**[Apache Netty:](https://netty.io/)** High-performance networking framework
[Video](https://www.youtube.com/watch?v=DKJ0w30M0vg) • [Video](https://www.youtube.com/watch?v=hvYqSz_BgUM)

---

## Currently Reading / Next Up

### AI Storage & ML Training Infrastructure

**[An RDMA-First Object Storage System with SmartNIC Offload:](https://arxiv.org/html/2509.13997v1#:~:text=Using%20FIO%2FDFS%20across%20local%20and,of%20RDMA%20for%20offloaded%20deployments)**
Low-latency storage for GPU workloads using RDMA and SmartNIC offloading

**[New Challenges of Benchmarking All-Flash Storage for HPC:](https://pdsw.org/pdsw21/papers/ws_pdsw_paper_S2_P1_paper-lockwood.pdf)**
Storage benchmarking methodologies for high-performance computing

**[Fire-Flyer AI-HPC:](https://arxiv.org/html/2408.14158v1)**
A Cost-Effective Software-Hardware Co-Design for Deep Learning


**[DAOS:](https://dl.acm.org/doi/10.1007/978-3-030-48842-0_3)**
 A Scale-Out High Performance Storage Stack for Storage Class Memory  • [Paper](https://dl.acm.org/doi/pdf/10.1145/3581576.3581577) • [Paper](https://arxiv.org/abs/2409.18682)


**[io_uring for High-Performance DBMSs: When and How to Use It:](https://arxiv.org/pdf/2512.04859v1)**
Modern Linux async I/O for database systems

**[Network and Storage Benchmarks for LLM Training on the Cloud:](https://maknee.github.io/blog/2025/Network-And-Storage-Training-Skypilot/#:~:text=Storage%20Type%20%20Read%20Speed,performance%20persistent%20storage)**
Comprehensive benchmarking for transformer model training

**[An Intro to DeepSeek's Distributed File System:](https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/)**
Novel distributed file system design for ML workloads

**[LLM Training Without a Parallel File System:](https://blog.glennklockwood.com/2025/02/llm-training-without-parallel-file.html)**
Alternative storage architectures for large language model training

**[A Reality Check on DeepSeek's Distributed File System Benchmarks:](https://maknee.github.io/blog/2025/3FS-Performance-Journal-2/)**
Critical analysis of benchmarking methodologies

---

## Research Interests & Future Topics

I'm actively seeking papers, collaborations, and speaking opportunities in:

- **RDMA-enabled storage for AI workloads**: GPU Direct Storage, NVMe-oF, network-attached accelerators
- **Caching hierarchies for ML training**: Tier-0 caching, pre-fetching strategies, cache coherency
- **Storage benchmarking for AI**: Standardized methodologies, Simulating realistic workloads patterns
- **Multi-protocol storage**: NFS/S3 unified access, POSIX semantics over object storage
- **Distributed systems performance**: Profiling, optimization & case studies

### Target Conferences

- **FAST** (File and Storage Technologies)
- **OSDI** (Operating Systems Design and Implementation)
- **SOSP** (Symposium on Operating Systems Principles)
- **SoCC** (Symposium on Cloud Computing)
- **NSDI** (Networked Systems Design and Implementation)
- **ATC** (Annual Technical Conference)
- **HotStorage** (Hot Topics in Storage)

---

*Interested in collaboration, co-authorship, or have paper recommendations? [Email me](mailto:sethi.hemant@gmail.com)*
