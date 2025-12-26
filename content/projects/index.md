---
title: "Projects"
layout: "single"
hideAuthor: true
---

My work spans AI storage optimization, distributed systems, and high-throughput data processing systems. Below are some key areas/projects I have been involved with.

### Multi-Protocol Storage for ML Workloads
Building and supporting storage systems that support both NFS (for legacy HPC workflows) and S3 (for cloud-native pipelines) over the same dataset. Key challenges include:
- Protocol semantic differences (POSIX vs object storage)
- Consistency models for concurrent access patterns
- Performance optimization for sequential reads (training) vs random access (checkpointing/Inference)

### Tier-0 Caching Strategies for GPU Clusters
Researching node-local caching architectures to minimize data transfer over network fabric:
- Pre-fetching strategies based on training iteration patterns
- Cache eviction policies
- RDMA integration for sub-microsecond latency data transfers
- Benchmarking with PyTorch DataLoader and TensorFlow data pipelines

### Storage Benchmarking for Transformer Training
Profiling storage I/O patterns for large language model training:
- Characterizing data loading bottlenecks in transformer architectures
- **Tools:** FIO, elbencho, custom PyTorch profilers
- Building Load Testing Frameworks on top of Elbencho to test File and Object storage.

### High-Throughput Streaming Data Ingestion and Delivery 
Scaling data ingestion pipeline to billions of events and delivery across thousands of Partitions(s3-prefixes):
- **Dynamic Partitioning redesign**: Akka Streams architecture achieving 400% throughput improvement
- Backpressure handling and flow control in reactive systems
- Lease management for distributed coordination
- SQS/DynamoDB for workload distribution and state management

### Performance Engineering
Approaches to performance optimization:
- Profiling Java services for memory leaks and GC tuning
- Native memory analysis, exploring various unix memory allocators(**malloc vs JEMalloc**) and heap dump investigation
- Identifying hot paths and optimizing critical sections
- Monitoring and observability for production systems

## Research Interests

Current areas of exploration and experimentation:
- **RDMA-enabled storage**: Low-latency data access for AI workloads
- **Caching hierarchies**: Multi-tier caching strategies (node-local, rack-level, datacenter)
- **Storage cost optimization**: Balancing performance and cost for training workloads
- **Benchmarking methodologies**: Standardized approaches for storage performance evaluation

## Technical Writing & Speaking

As an aspiring technical author, I'm interested in writing about:
- Storage architecture for AI/ML infrastructure
- Distributed systems design patterns
- Performance optimization techniques
- Real-world case studies from production systems

*Interested in collaboration, co-authorship, or speaking opportunities? [Reach out](mailto:sethi.hemant@gmail.com).*