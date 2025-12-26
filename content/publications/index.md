---
title: "Publications"
layout: "single"
hideAuthor: true
---

I'm working on publishing technical papers and giving talks on storage systems being built for the new wave of AI/ML infrastructure.

## Research Areas

### AI Storage Optimization
- **RDMA-enabled object storage**: How to get sub-microsecond latency for GPU training workloads
- **Tier-0 caching**: Pre-fetching and eviction policies for transformer training access patterns
- **Multi-protocol storage**: Making NFS and S3 work on the same data without breaking consistency

### Distributed Systems Performance
- **Storage benchmarking**: Building tools that measure what actually matters for ML workloads (not just random IOPS)
- **High-throughput streaming**: Scaling data pipelines to billions of events using Akka Streams and reactive patterns

## Working On

- **Storage benchmarking for frontier model training**: What metrics actually matter when you're loading 100TB+ datasets
- **RDMA performance in production**: Real-world numbers from GPU clusters, not vendor benchmarks
- **Tier-0 caching patterns**: When pre-fetching helps and when it doesn't
- **Multi-protocol storage tradeoffs**: The consistency problems nobody talks about

## Looking For

- **Co-authors** for papers on storage systems or ML infrastructure
- **Speaking slots** at FAST, OSDI, SoCC, MLSys, or practitioner conferences
- **Peer review** opportunities (I'll review papers on distributed systems, storage, or ML infrastructure)
- **Collaboration** on open-source benchmarking tools or storage projects

If you're organizing conferences, running workshops, or writing papers in this space—or if you just want to talk about storage performance—reach out.

### Academic & Industry Interests
My research draws inspiration from foundational distributed systems work (Dynamo, Spanner, GFS, Raft, Tao, Memcached) and aims to bridge academic research with real-world production challenges in AI infrastructure.

---

*If you're working on related research or organizing conferences/workshops in these areas, I'd love to connect: [sethi.hemant@gmail.com](mailto:sethi.hemant@gmail.com)*