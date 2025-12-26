---
title: "About Me"
layout: "single"
hideAuthor: true
---

I'm a Staff Software Engineer with 12+ years building high-performance data platforms and AI storage infrastructure. I work at the intersection of distributed systems and machine learning, focusing on keeping expensive GPUs fed with data.

At Crusoe, I am building S3-compatible object storage with node-local(Tier-0) caching for ML training and inference workloads. My work centers on minimizing data access latency for the GPUs and solve storage bottlenecks which directly impact training costs by minimizing GPU Idle time, which is the largest contributor to the TCO of an AI Datacenter.

At AWS, I led the Dynamic Partitioning migration for Amazon Firehose, rearchitecting the service to handle high-throughput delivery across thousands of S3 prefixes. This meant redesigning partitioning logic with Akka Streams (which achieved 4x throughput gains, and 10x default partition count gains), solving some nasty native memory leaks in Java services, and tuning GC behavior under production load.

At WeWork, I migrated the Spatial Data Service from PHP to Go/gRPC/Kubernetes, dropping P99 latency to 100ms for a system serving 800+ locations worldwide. I also built out Kafka-based event streaming with Avro schemas and built out the service's observability stack using Prometheus, Grafana and Jaegar.

## What Drives Me

Storage is the unglamorous bottleneck in AI infrastructure. Everyone talks about GPU clusters and model architectures, but the hardest problems are often in moving petabytes of training data fast enough to keep those GPUs saturated. I work on the boring parts that make the exciting parts possible: RDMA-enabled object stores, pre-fetching strategies for transformer training, benchmarking tools that actually measure what matters.

I spend a lot of time reading foundational papers like Dynamo, Spanner, GFS, Raft and figuring out how those ideas apply (or don't) to modern ML workloads. The patterns are familiar but the scale and access patterns are different enough to require new approaches.

I'm looking for opportunities to publish, present at conferences, and collaborate with researchers working on similar problems. If you're writing papers on storage systems, organizing FAST/OSDI/SOSP sessions, or need peer reviewers for storage-related work, let's talk.

## Technical Interests

- **Languages**: Golang, Java, Python
- **Infrastructure**: Kubernetes, Kafka, Distributed Data Systems especially Databases.
- **DevOps**: CI/CD, Infrastructure as Code, Observability
- **Research/Current Interest Areas**: RDMA storage, GPU cluster optimization, Multi-protocol access patterns

## Education

**B.Tech in Computer Science**
National Institute of Technology, Jalandhar | 2012

## Connect

- Email: [sethi.hemant@gmail.com](mailto:sethi.hemant@gmail.com)
- LinkedIn: [linkedin.com/in/hemantsethi](https://www.linkedin.com/in/hemantsethi/)
- GitHub: [github.com/roolerzz](https://github.com/roolerzz)
- Twitter: [@sethihemant](https://twitter.com/sethihemant)