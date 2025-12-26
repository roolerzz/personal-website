---
title: "Experience"
layout: "single"
hideAuthor: true
---

## Staff Software Engineer (Storage)
**Crusoe Energy Systems(Crusoe AI)**

Leading architecture and development of Crusoe's AI-optimized object storage platform for high-performance data access in GPU-intensive ML workloads.

- Implementing dual-protocol storage supporting both NFS and S3 access patterns over unified datasets, enabling seamless integration with legacy HPC workflows and modern cloud-native AI pipelines
- Designing and implementing intelligent node-local (Tier-0) caching and pre-fetching strategies to minimize data access latency, reducing data bottleneck time and increasing GPU utilization to reduce cost-per-GPU-hour (TCO)
- Benchmarking and profiling storage access patterns for model training/inference workloads and PyTorch/TensorFlow data loading pipelines to identify and eliminate storage bottlenecks impacting GPU utilization
- Supporting multi-cluster, multi-vendor storage system enabling rapid deployment of new storage clusters

---

## Software Development Engineer
**Amazon Web Services**

Led architectural initiatives for Amazon Data Firehose, serving enterprise customers processing billions of events daily.

- Led the architectural migration of Firehose's Dynamic Partitioning to microservices-based Gen2 architecture, driving scalability and operational efficiency while managing a team of 5 engineers
- Redesigned partitioning and scaling strategy, increasing per-partition throughput by 400% and partition count by 1000% using Akka's PartitionHub/MapAsync, eliminating manual scaling interventions and customer escalations
- Led improvements in Data Processing framework enabling efficient workload offloading and streamlining data transformations using SQS, DynamoDB/Redis Pub-Sub
- Implemented generic lease management library to support multiple services during Gen2 migration across Firehose's backend services
- Led performance optimization initiatives, profiling Java services to diagnose and resolve native memory leaks causing high GC/CPU utilization
- Improved operational posture by defining SOPs, dashboards, and alarms, reducing MTTR for high-severity incidents
- Spearheaded Load Balancer migration from hardware-based VIPs to ELBs, reducing costs, enabling on-demand scaling, and cutting expansion time from months to days
- Led Firehose region expansion in KIX with 3 engineers, introducing automations that reduced region launch times by 67%
- Mentored engineers across teams through technical deep dives and onboarding sessions, fostering engineering excellence

---

## Software Engineer
**WeWork**

Migrated WeWork's legacy PHP-based space service to Go/gRPC/Protocol Buffers/Kubernetes-based microservices architecture as part of a 5-engineer team.

- Reduced latency by 90%, achieving P99 latency of 100ms for spatial data service serving as source of truth for all spatial data at WeWork
- Supported core business use cases including inventory management and occupancy map visualization across 800+ global locations
- Integrated Kafka-based event-driven system to synchronize spatial data with downstream services, ensuring real-time data updates for Inventory Management
- Used Apache Avro for data serialization and schema registry for schema enforcement for Kafka events
- Implemented observability (logs, metrics, traces, dashboards) using Jaeger, Prometheus, and Grafana

---