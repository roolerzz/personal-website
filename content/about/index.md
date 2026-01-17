---
title: "About Me"
layout: "single"
hideAuthor: true
---

I’m a Staff Software Engineer at Crusoe, where I help develop storage solutions for running AI/ML workloads for our customers and helping keep the GPUs fed. My current work involves evaluating and integrating storage solutions such as RDMA-enabled object stores, multi-protocol systems, node-local caching etc and making those available to our customers.

The most interesting problems in AI infrastructure aren't in the models; they're in keeping GPUs fed with data. I focus on the bottlenecks: deep evaluation of competing approaches (RDMA vs. traditional networking, object vs. file interfaces), performance benchmarking against real transformer training patterns, and making architectural recommendations that affect millions in infrastructure spending.

Previously at **AWS**, I led the Dynamic Partitioning migration for Amazon Firehose, rearchitecting the service to handle high-throughput delivery across thousands of S3 prefixes, achieving 4x throughput gains and 10x partition count improvements.

## Current Work

**Storage for GPU Clusters:**
- Evaluating and integrating vendor backed storage solution(multi-protocol: NFS, S3, SMB)
- Designing node-local caching strategies to minimize network transfer
- Benchmarking storage performance (FIO, elbencho, PyTorch DataLoader profiling)
- Building custom middleware for optimizing data access patterns

**Research Interests:**
- RDMA-enabled storage architectures for sub-microsecond latency
- Storage benchmarking methodologies (FIO/Elbencho/MLCommons for AI workloads)
- Cost-performance tradeoffs in GPU cluster storage
- Multi-protocol access patterns (POSIX, S3, NFS) over unified datasets

## Writing & Speaking

I am going to maintain comprehensive [technical notes](/notes/) on various distributed systems papers that I am reading, as well as publish [blog posts](/posts/) on analyzing storage architectures for AI workloads.

**Open to:**
- Conference speaking opportunities such as (USENIX, OSDI, MLSys, HotStorage, SREcon)
- Peer review **(Or Artifact Evaluation Committees)** roles for storage/systems conferences and journals
- Collaboration on open-source benchmarking tools or storage research

## Connect

- **Email**: [sethi.hemant@gmail.com](mailto:sethi.hemant@gmail.com)
- **LinkedIn**: [linkedin.com/in/hemantsethi](https://www.linkedin.com/in/hemantsethi/)
- **GitHub**: [github.com/roolerzz](https://github.com/roolerzz)
- **Twitter**: [@sethihemant](https://twitter.com/sethihemant)
