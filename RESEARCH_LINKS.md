# Research Links & References

This document contains all paper links, author profiles, and resources mentioned in the research compilation.

---

## 2. Complete Links & References

### Recent AI Storage Papers (2023-2025)

#### RDMA & GPU Storage

**Predictive Load Balancing for RDMA Traffic** (2025)
- Paper: https://arxiv.org/html/2506.08132v1
- Meta AI cluster analysis with up to 128 GPUs

**An RDMA-First Object Storage System with SmartNIC Offload** (DeepSeek, 2025)
- Paper: https://arxiv.org/html/2509.13997v1
- DeepSeek 3FS architecture

**RDMA over Ethernet for Distributed Training at Meta Scale** (SIGCOMM 2024)
- Paper: https://dl.acm.org/doi/10.1145/3651890.3672233
- Real-world RDMA deployment at Meta

**An Extensible Software Transport Layer for GPU Networking** (2025)
- Paper: https://arxiv.org/html/2504.17307v1

**GPUVM: GPU-driven Unified Virtual Memory** (2024)
- Paper: https://arxiv.org/pdf/2411.05309
- Authors: Nurlan Nazaraliyev, Elaheh Sadredini

**Storage Access Optimization for Efficient GPU-Centric Information Retrieval** (2025)
- Paper: https://link.springer.com/article/10.1007/s11227-025-07118-9
- Journal of Supercomputing

**GMT: GPU Orchestrated Memory Tiering for the Big Data Era** (2024)
- Paper: https://www.researchgate.net/publication/380151066_GMT_GPU_Orchestrated_Memory_Tiering_for_the_Big_Data_Era

**Democratizing AI: Open-source Scalable LLM Training on GPU-based Supercomputers** (SC 2024)
- Paper: https://dl.acm.org/doi/10.1109/SC41406.2024.00010

#### Object Storage for AI Training

**Very Large AI Model Training Uses Object Storage** (2025)
- Article: https://blocksandfiles.com/2025/02/04/very-large-ai-model-training-uses-object-storage/
- Microsoft research showing object storage advantages

**Network and Storage Benchmarks for LLM Training on the Cloud** (2025)
- Blog: https://maknee.github.io/blog/2025/Network-And-Storage-Training-Skypilot/

**NFS to JuiceFS: Building a Scalable Storage Platform for LLM Training & Inference** (2024-2025)
- Case study: https://juicefs.com/en/blog/user-stories/ai-storage-platform-large-language-model-training-inference

**Benchmarking S3 for AI Workloads - VAST Data** (2024-2025)
- Blog: https://www.vastdata.com/blog/benchmarking-s3-ai-workloads-optimizing-checkpointing-data-access

**Efficient Training of Large Language Models on Distributed Infrastructures: A Survey** (2024)
- Paper: https://arxiv.org/html/2407.20018v1
- Comprehensive survey of LLM training infrastructure

**A Look Into Training Large Language Models on Next Generation Datacenters** (2024)
- Paper: https://arxiv.org/html/2407.12819v1

**Fire-Flyer AI-HPC: A Cost-Effective Software-Hardware Co-Design for Deep Learning** (2024)
- Paper: https://arxiv.org/html/2408.14158v2

#### Caching & Data Loading

**Baleen: ML Admission & Prefetching for Flash Caches** (FAST 2024)
- Blog: https://www.cs.cmu.edu/~csd-phd-blog/2023/baleen-ml-flash-caching/
- CMU research

**Machine Learning for Flash Caching in Bulk Storage Systems** (CMU 2024)
- Report: http://reports-archive.adm.cs.cmu.edu/anon/2024/CMU-CS-24-152.pdf
- Technical Report CMU-CS-24-152
- Author: Daniel Lin-Kit Wong

**NoPFS: Clairvoyant Prefetching for Distributed Machine Learning I/O** (2021)
- Paper: https://arxiv.org/pdf/2101.08734

**HVAC: Removing I/O Bottleneck for Large-Scale Deep Learning Applications**
- Report: https://www.osti.gov/servlets/purl/1902810

**Optimizing I/O for AI Workloads in Geo-Distributed GPU Clusters** (Alluxio, 2024)
- Whitepaper: https://www.alluxio.io/whitepaper/optimizing-i-o-for-ai-workloads-in-geo-distributed-gpu-clusters

**StellaTrain: Accelerating Model Training in Multi-cluster Environments** (SIGCOMM 2024)
- Paper: https://dl.acm.org/doi/10.1145/3651890.3672228

**SiloD: A Co-design of Caching and Scheduling for Deep Learning Clusters** (EuroSys 2023)
- Conference: EuroSys 2023

**SHADE: Enable Fundamental Cacheability for Distributed Deep Learning Training** (FAST 2023)
- Conference: USENIX FAST 2023

**iCACHE: An Importance-Sampling-Informed Cache for Accelerating I/O-Bound DNN Model Training** (HPCA 2023)
- Conference: HPCA 2023

**FFCV: Accelerating Training by Removing Data Bottlenecks** (CVPR 2023)
- Paper: https://openaccess.thecvf.com/content/CVPR2023/papers/Leclerc_FFCV_Accelerating_Training_by_Removing_Data_Bottlenecks_CVPR_2023_paper.pdf
- Authors: Guillaume Leclerc et al.
- GitHub: https://github.com/libffcv/ffcv
- Docs: https://docs.ffcv.io/

**NVIDIA DALI (Data Loading Library)**
- GitHub: https://github.com/NVIDIA/DALI
- Developer: https://developer.nvidia.com/dali

#### Storage Benchmarking

**MLPerf Storage v2.0 Benchmark Results** (August 2025)
- Results: https://mlcommons.org/2025/08/mlperf-storage-v2-0-results/
- Includes Llama 3.1 405B benchmarks

**MLPerf Storage v1.0 Benchmark Results** (September 2024)
- Results: https://mlcommons.org/2024/09/mlperf-storage-v1-0-benchmark-results/

**Introducing the MLPerf Storage Benchmark Suite** (June 2023)
- Announcement: https://mlcommons.org/2023/06/introducing-the-mlperf-storage-benchmark-suite/

**MLPerf Storage Working Group**
- Homepage: https://mlcommons.org/working-groups/benchmarks/storage/

**Forecasting GPU Performance for Deep Learning Training and Inference** (2024)
- Paper: https://dl.acm.org/doi/abs/10.1145/3669940.3707265
- ASPLOS 2025

#### Multi-Protocol Storage

**The Case for Dual-access File Systems over Object Storage** (HotStorage 2019)
- Paper: https://www.usenix.org/system/files/hotstorage19-paper-lillaney.pdf
- Authors: Lillaney et al.

**CunoFS: Bringing Posix File Access to S3 Object Storage** (2024)
- Article: https://www.computerweekly.com/news/366545495/CunoFS-brings-Posix-file-access-to-S3-object-storage-capacity

**IBM Storage Scale S3** (2024)
- Documentation: https://www.ibm.com/docs/en/storage-scale/6.0.0?topic=sso-multi-protocol-data-sharing-s3-nfs-smb-posix-storage-scale-container-storage-interface-driver

**Future of Storage for HPC and AI: Rise of Objects, Metadata, and AI-Ready Storage** (2025)
- Article: https://www.hpcwire.com/2025/10/29/future-of-storage-for-hpc-and-ai-rise-of-objects-metadata-and-ai-ready-storage/

**Unified File and Object Storage: Three Suppliers and Their Approaches**
- Article: https://www.computerweekly.com/feature/Unified-file-and-object-storage-Three-suppliers-and-their-approaches

#### Checkpoint Storage

**Inshrinkerator: Compressing Deep Learning Training Checkpoints via Dynamic Quantization** (SoCC 2024)
- Paper: https://dl.acm.org/doi/10.1145/3698038.3698553

**Check-QZP: A Lightweight Checkpoint Mechanism for Deep Learning Frameworks** (2024)
- Paper: https://www.mdpi.com/2076-3417/14/19/8848
- MDPI Applied Sciences

**Research on Storage Optimization for Efficient Training of Large Language Models** (2025)
- Paper: https://link.springer.com/article/10.1007/s11280-025-01367-7
- World Wide Web Journal
- Introduces LMStor

**Just-In-Time Checkpointing: Low Cost Error Recovery from Deep Learning Training Failures** (EuroSys 2024)
- Paper: https://dl.acm.org/doi/10.1145/3627703.3650085
- Microsoft Research

**Check-N-Run: a Checkpointing System for Training Deep Learning Recommendation Models** (NSDI 2022)
- Paper: https://www.usenix.org/conference/nsdi22/presentation/eisenman
- Authors: Eisenman et al.

---

### Classic Distributed Systems Papers

**Dynamo: Amazon's Highly Available Key-value Store** (SOSP 2007)
- Paper: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Werner Vogels' website: https://www.allthingsdistributed.com/

**Cassandra: A Decentralized Structured Storage System** (2009)
- Paper: https://research.cs.cornell.edu/ladis2009/papers/lakshman-ladis2009.pdf
- Apache Cassandra: https://cassandra.apache.org/
- Internals video: https://www.youtube.com/watch?v=uossfVwxWXk
- Read path: https://www.youtube.com/watch?v=HuDJBTPdaOA
- Performance tuning: https://www.scnsoft.com/data/cassandra-performance
- Documentation: https://cassandra.apache.org/doc/latest/

**DynamoDB: Amazon's Highly Available Key-value Store (2022 update)**
- Paper: https://www.usenix.org/conference/atc22/presentation/elhemali
- AWS re:Invent talks: Search "DynamoDB deep dive" on YouTube

**Spanner: Google's Globally-Distributed Database** (OSDI 2012)
- Paper: https://research.google/pubs/pub39966/
- Research page: https://research.google.com/archive/spanner.html

**Bigtable: A Distributed Storage System for Structured Data** (OSDI 2006)
- Paper: https://research.google/pubs/pub27898/
- Research page: https://research.google.com/archive/bigtable.html

**Megastore: Providing Scalable, Highly Available Storage for Interactive Services** (CIDR 2011)
- Paper: https://research.google/pubs/pub36971/

**The Google File System** (SOSP 2003)
- Paper: https://research.google/pubs/pub51/

**The Hadoop Distributed File System** (2010)
- Paper: https://storageconference.us/2010/Papers/MSST/Shvachko.pdf
- Apache HDFS: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html

**The Chubby Lock Service for Loosely-Coupled Distributed Systems** (OSDI 2006)
- Paper: https://research.google/pubs/pub27897/

**Paxos Made Simple** (2001)
- Paper: https://lamport.azurewebsites.net/pubs/paxos-simple.pdf
- Lamport's website: https://lamport.azurewebsites.net/

**Paxos Made Live - An Engineering Perspective** (PODC 2007)
- Paper: https://research.google/pubs/pub33002/

**In Search of an Understandable Consensus Algorithm (Raft)** (2014)
- Paper: https://raft.github.io/raft.pdf
- Raft website: https://raft.github.io/
- Visualization: https://raft.github.io/

**Time, Clocks, and the Ordering of Events in a Distributed System** (Lamport, 1978)
- Paper: https://lamport.azurewebsites.net/pubs/time-clocks.pdf

**Kafka: A Distributed Messaging System for Log Processing** (2011)
- Paper: http://notes.stephenholiday.com/Kafka.pdf
- Apache Kafka: https://kafka.apache.org/
- Documentation: https://kafka.apache.org/documentation/

**MapReduce: Simplified Data Processing on Large Clusters** (OSDI 2004)
- Paper: https://research.google/pubs/pub62/

**Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing (Spark)** (NSDI 2012)
- Paper: https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf
- Apache Spark: https://spark.apache.org/

**Apache Flink: Stream and Batch Processing in a Single Engine** (2015)
- Paper: https://arxiv.org/pdf/1506.05202
- Apache Flink: https://flink.apache.org/

**Scaling Memcache at Facebook** (NSDI 2013)
- Paper: https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf
- Nishtala talk: https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala

**TAO: Facebook's Distributed Data Store for the Social Graph** (ATC 2013)
- Paper: https://www.usenix.org/system/files/conference/atc13/atc13-bronson.pdf
- Nathan Bronson talk: https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson

**Redis Documentation**
- Homepage: https://redis.io/
- Documentation: https://redis.io/docs/

**Elasticsearch: The Definitive Guide**
- Homepage: https://www.elastic.co/
- Documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

**The Snowflake Elastic Data Warehouse** (SIGMOD 2016)
- Paper: https://dl.acm.org/doi/10.1145/2882903.2903741
- Snowflake: https://www.snowflake.com/

**Zuul 2: The Netflix Journey to Asynchronous, Non-Blocking Systems**
- Blog: https://netflixtechblog.com/zuul-2-the-netflix-journey-to-asynchronous-non-blocking-systems-45947377fb5c
- GitHub: https://github.com/Netflix/zuul

**Apache Netty**
- Homepage: https://netty.io/
- GitHub: https://github.com/netty/netty

---

### Open Source Projects

**JuiceFS**
- Homepage: https://juicefs.com/
- GitHub: https://github.com/juicedata/juicefs (11k+ stars)
- Documentation: https://juicefs.com/docs/community/
- JuiceFS vs Alluxio comparison: https://juicefs.com/docs/community/comparison/juicefs_vs_alluxio/
- NAVER case study: https://juicefs.com/en/blog/user-stories/juicefs-vs-alluxio-ai-storage-naver
- 2024 Recap: https://juicefs.com/en/blog/company/2024-recap-artificial-intelligence-storage

**Alluxio**
- Homepage: https://www.alluxio.io/
- GitHub: https://github.com/Alluxio/alluxio
- Documentation: https://docs.alluxio.io/

**FFCV (Fast Forward Computer Vision)**
- Homepage: https://ffcv.io/
- GitHub: https://github.com/libffcv/ffcv
- Documentation: https://docs.ffcv.io/
- Paper: https://openaccess.thecvf.com/content/CVPR2023/papers/Leclerc_FFCV_Accelerating_Training_by_Removing_Data_Bottlenecks_CVPR_2023_paper.pdf

**NVIDIA DALI**
- GitHub: https://github.com/NVIDIA/DALI
- Developer page: https://developer.nvidia.com/dali

**Storage-for-AI-Paper Collection (GitHub)**
- Repository: https://github.com/hegongshan/Storage-for-AI-Paper
- Curated list of must-read papers

**ML Systems Papers Collection (GitHub)**
- Repository: https://github.com/byungsoo-oh/ml-systems-papers
- Broader ML systems research

**MinIO**
- Homepage: https://min.io/
- GitHub: https://github.com/minio/minio
- Documentation: https://min.io/docs/minio/linux/index.html
- AI solutions: https://www.min.io/solutions/object-storage-for-ai

---

### Active Researchers

**Youyou Lu** (Tsinghua University)
- Homepage: https://storage.cs.tsinghua.edu.cn/~lu/
- Publications: http://storage.cs.tsinghua.edu.cn/~lu/pub.html/
- Google Scholar: Search "Youyou Lu Tsinghua"
- Research group: https://storage.cs.tsinghua.edu.cn/

**Jiwu Shu** (Tsinghua University)
- Homepage: https://storage.cs.tsinghua.edu.cn/~jiwu-shu/
- Research group: https://storage.cs.tsinghua.edu.cn/

**Swaminathan Sundararaman** (IBM Research)
- Google Scholar: https://scholar.google.com/citations?user=7sWDfEYAAAAJ&hl=en
- IBM Research page: Search "Swaminathan Sundararaman IBM Research"

**Chenxi Yang, Yan Li, Martin Maas** (Google)
- MLSys 2025 paper: Cross-Layer ML-Based Storage Optimization
- Google Research: https://research.google/

**K. V. Rashmi** (Carnegie Mellon University)
- Homepage: https://www.cs.cmu.edu/~rvinayak/
- CMU page: https://www.cs.cmu.edu/~rvinayak/

**Guillaume Leclerc** (MIT)
- Personal page: Search "Guillaume Leclerc MIT FFCV"
- FFCV project: https://ffcv.io/

**Daniel Lin-Kit Wong** (CMU)
- CMU page: Search "Daniel Wong CMU"
- Thesis: Machine Learning for Flash Caching

---

### Industry Solutions & Vendors

**WEKA**
- Homepage: https://www.weka.io/
- Blog: https://www.weka.io/blog/
- Performance: 600+ GB/s, 5M IOPS

**VAST Data**
- Homepage: https://www.vastdata.com/
- Blog: https://www.vastdata.com/blog/
- Crusoe partnership: https://www.datacenterdynamics.com/en/news/crusoe-partners-with-vast-data-for-high-performance-storage-on-crusoe-cloud/
- Blocks & Files coverage: https://blocksandfiles.com/2024/09/30/clean-living-crusoe-scales-up-its-ai-cloud-with-vast-data-systems/

**DDN (DataDirect Networks)**
- Homepage: https://www.ddn.com/
- Lustre: https://www.lustre.org/

**IBM Storage Scale (GPFS)**
- Homepage: https://www.ibm.com/storage/scale
- Documentation: https://www.ibm.com/docs/en/storage-scale

**Scality RING**
- Homepage: https://www.scality.com/
- Documentation: https://www.scality.com/products/ring/

---

### Conferences

**USENIX FAST (File and Storage Technologies)**
- Homepage: https://www.usenix.org/conferences/byname/146
- FAST 2024: https://www.usenix.org/conference/fast24
- FAST 2025: https://www.usenix.org/conference/fast25
- FAST 2026 CFP: https://www.usenix.org/conference/fast26/call-for-papers

**USENIX OSDI (Operating Systems Design and Implementation)**
- Homepage: https://www.usenix.org/conferences/byname/179
- OSDI 2024: https://www.usenix.org/conference/osdi24
- OSDI 2025: https://www.usenix.org/conference/osdi25
- OSDI 2026 CFP: https://www.usenix.org/sites/default/files/osdi26_cfp_120325.pdf

**ACM SOSP (Symposium on Operating Systems Principles)**
- Homepage: https://sigops.org/s/conferences/sosp/
- SOSP 2024: https://sigops.org/s/conferences/sosp/2024/

**ACM SoCC (Symposium on Cloud Computing)**
- Homepage: https://acmsocc.org/
- Recent proceedings: https://dl.acm.org/conference/socc

**USENIX ATC (Annual Technical Conference)**
- Homepage: https://www.usenix.org/conferences/byname/131
- ATC 2024: https://www.usenix.org/conference/atc24
- ATC 2025: https://www.usenix.org/conference/atc25

**ACM NSDI (Networked Systems Design and Implementation)**
- Homepage: https://www.usenix.org/conferences/byname/178
- NSDI 2025: https://www.usenix.org/conference/nsdi25

**HotStorage**
- Homepage: https://www.hotstorage.org/
- HotStorage 2024: https://www.hotstorage.org/2024/
- HotStorage 2025: https://www.hotstorage.org/

**MLSys Conference**
- Homepage: https://mlsys.org/
- MLSys 2025: https://mlsys.org/virtual/2025/papers.html

**ACM SIGCOMM**
- Homepage: https://www.sigcomm.org/
- Conference page: https://conferences.sigcomm.org/

---

### Books

**Designing Data-Intensive Applications** by Martin Kleppmann
- Official site: https://dataintensive.net/
- Publisher: https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/
- Author's website: https://martin.kleppmann.com/

**Database Internals** by Alex Petrov
- Official site: https://www.databass.dev/
- Publisher: https://www.oreilly.com/library/view/database-internals/9781492040330/
- GitHub: https://github.com/ifesdjeen/database-internals

**A Philosophy of Software Design** by John Ousterhout
- Official site: https://web.stanford.edu/~ouster/cgi-bin/book.php
- Stanford page: https://web.stanford.edu/~ouster/

---

### Videos & Talks

**Jordan Has No Life (YouTube Channel)**
- Channel: https://www.youtube.com/@jordanhasnolife5163
- Covers: Cassandra, HBase, BigTable, Spanner, Chubby, GFS, Paxos, Megastore

**Papers We Love**
- Homepage: https://paperswelove.org/
- YouTube: https://www.youtube.com/@PapersWeLove
- GitHub: https://github.com/papers-we-love/papers-we-love

**HelloInterview (System Design Deep Dives)**
- YouTube: https://www.youtube.com/@hello_interview
- Covers: Redis, Elasticsearch, Cassandra deep dives

**CMU Database Group (Andy Pavlo)**
- YouTube: https://www.youtube.com/@CMUDatabaseGroup
- Database lectures and talks

---

### Additional Resources

**Blocks and Files (Storage Industry News)**
- Homepage: https://blocksandfiles.com/
- AI storage coverage: https://blocksandfiles.com/category/ai/

**The Morning Paper (Research Paper Summaries)**
- Archive: https://blog.acolyer.org/
- Daily summaries of CS research papers (archived)

**Hacker News**
- Homepage: https://news.ycombinator.com/
- Search for papers and discussions

**arXiv.org (Preprints)**
- CS Distributed Computing: https://arxiv.org/list/cs.DC/recent
- CS Performance: https://arxiv.org/list/cs.PF/recent
- CS Systems: Search cs.DC, cs.PF, cs.OS

**ACM Digital Library**
- Homepage: https://dl.acm.org/

**USENIX Publications**
- Homepage: https://www.usenix.org/publications

---

## Usage Notes

1. **For website updates**: Copy relevant links into your Research page
2. **For paper reading**: Use these links as starting points for deep dives
3. **For collaboration**: Researcher homepages include contact information
4. **For conferences**: Subscribe to CFP notifications from target venues

---

Last updated: December 2024
Compiled for: Hemant Sethi's EB-1A research portfolio
