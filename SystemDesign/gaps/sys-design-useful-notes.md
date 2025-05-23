
# Scaling high traffic

## Load Balancer

Reliability - What happens when a load balancer goes down?

- Redirect to another load balancer
- How do we know it goes down? HeartBeat, or Zookeeper

## Compute Platform

- Horiztonally scale with load balancer

## Data store

### NoSQL

- Use if you need kev value pair storage
- Scales easily
- Good for read heavy systems
- Optimized for high write throughput
- Eventual consistency
- BASE
  - Base means **eventual consistency**

### SQL

- Scales harder
  - sharding
    - shard key
      - break up db to pieces
      - using userId normally, user should stay on one shard (otherwise sharding is redundant)
  - read replicates
    - async updates data from primary to replicas if eventual consisteny is allowed 
- Consistent
  - ACID
  - Isolation means if two db updates at the same time there is order
    - wiht locking, there is no conlficts, this happens in NoSQL
- Joins
  - If your reads need Joins, you need SQL
    - Ex Twitter user table joined with tweet table

### CAP

Consistency

Availability

Partition

- If there is a partition in the system (replication)
- If one node gets put to one node, but not another node yet. If a read where to happen on the wrong node, the data is not consistent.
- We can lock the node with the stale data down, but that will impact availability


PACELC: Todo this

## Caching

## Object storage / CDN

- Store media in object storage
- Use CDN to bring assets closer to customer

### CDN Algorithms

- Push: Customers need the data readily fast
- Pull: Customers pull data closer to them to help next person


## HTTP Headers / Authentications

### Authorization token


---

# How to scale a SQL db?

Read only Replicas

Sharing



# NoSQL databases tend to handle large-scale data better than SQL databases.
    - Scalability
    - Data model flexibility
    - Throughput and Low-Latency: For certain operations, especially simple data retrievals
    - Distribution and Fault Tolerance: Many NoSQL databases are designed to handle replication and distribution across multiple nodes


# SQL databases are still strong contenders for scale in scenarios where data cons
istency, complex querying, and transaction guarantees are essential


weakness
in hashinh knowlege

weakness in constistent hashing


