---
title: "About Me"
layout: "single"
hideAuthor: true
---

I'm a Staff Infrastructure Engineer at Crusoe, where I architect storage strategies for GPU training clusters. My work involves evaluating and integrating cutting-edge solutions—from RDMA-enabled object stores to multi-protocol file systems—while building custom middleware to optimize for AI training workload characteristics.

The most interesting problems in AI infrastructure aren't in the models—they're in keeping GPUs fed with data. I focus on the bottlenecks: deep evaluation of competing approaches (RDMA vs. traditional networking, object vs. file interfaces), performance benchmarking against real transformer training patterns, and making architectural recommendations that affect millions in infrastructure spending.

I bridge academic research and production deployment by publishing technical analyses of distributed systems papers and applying those principles to modern AI storage challenges. My writing connects foundational systems research (Dynamo, Spanner, GFS, Raft) to current problems in ML infrastructure, with a focus on what actually works versus vendor marketing claims.

Previously, at **AWS**, I led the Dynamic Partitioning migration for Amazon Firehose, rearchitecting the service to handle high-throughput delivery across thousands of S3 prefixes. This involved redesigning partitioning logic with Akka Streams, achieving 4x throughput gains and 10x partition count improvements while solving native memory leaks and GC issues.

## Looking to Collaborate

I'm actively seeking opportunities to:
- **Publish** technical papers and case studies (conferences, journals, workshops)
- **Present** at conferences (USENIX, OSDI/SOSP, MLSys, HotStorage, SREcon, storage/AI infrastructure venues)
- **Review** papers for journals and conferences
- **Collaborate** with researchers working on storage systems, benchmarking methodologies, or AI infrastructure

If you're organizing conference sessions, need peer reviewers for storage-related work, or want to discuss production insights from AI infrastructure deployment, please reach out.

## Technical Background

**Current Focus:**
- S3-compatible object storage with node-local caching for ML workloads
- Storage vendor evaluation and integration (RDMA, NVMe-oF, parallel file systems)
- Performance benchmarking (FIO, elbencho, PyTorch DataLoader profiling)
- Custom middleware for optimizing GPU training data access patterns

**Research Interests:**
- RDMA-enabled storage architectures
- Multi-protocol access patterns (POSIX, S3, NFS)
- Storage benchmarking methodologies for AI workloads
- Cost-performance tradeoffs in GPU cluster storage

**Technical Stack:**
- **Languages**: Go, Java, Python, Scala
- **Infrastructure**: Kubernetes, Kafka, Distributed Databases, Object Storage
- **Specializations**: High-throughput data systems, stream processing, distributed storage

## Education

**B.Tech in Computer Science**
National Institute of Technology, Jalandhar | 2012

## Writing & Research

I maintain comprehensive [technical notes](/notes/) on distributed systems papers and publish [blog posts](/posts/) analyzing storage architectures for AI workloads. Recent topics include admission control patterns from DynamoDB applied to AI storage, benchmarking methodology gaps for ML training, and RDMA storage evaluation frameworks.

## Connect

- **Email**: [sethi.hemant@gmail.com](mailto:sethi.hemant@gmail.com)
- **LinkedIn**: [linkedin.com/in/hemantsethi](https://www.linkedin.com/in/hemantsethi/)
- **GitHub**: [github.com/roolerzz](https://github.com/roolerzz)
- **Twitter**: [@sethihemant](https://twitter.com/sethihemant)

---

*Interested in collaboration, co-authorship, speaking opportunities, or peer review? Email me—I'm always happy to discuss storage systems and AI infrastructure.*