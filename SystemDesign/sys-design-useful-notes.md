
# Scaling high traffic

## Compute Platform

- Horiztonally scale with load balancer

## Data store


### NoSQL

- Scales easily
- Good for read heavy systems
- Optimized for high write throughput
- Eventual consistency

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
- Joins
  - If your reads need Joins, you need SQL

## Caching

## Object storage / CDN

- Store media in object storage
- Use CDN to bring assets closer to customer

### CDN Algorithms

- Push: Customers need the data readily fast
- Pull: Customers pull data closer to them to help next person


## HTTP Headers / Authentications

### Authorization token