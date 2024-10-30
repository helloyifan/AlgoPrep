# Key-Value Store

A db can be relational or non relational


No SQL databases can be much more flexibilty

* Graph
* Document
* KV stores
* Zookeeper is technically a kv store but its for coodination 

## Functional

Document DB

### APIs

* get(key)
* put(key, val)
* delete(key)


## Non Functional

Durableability

But not other aspects of ACID is needed
    - Ie NoSQL has no Isolation, nosql has no locking mechanisms


## Design Detail


### Indexing data

LSM trees

* Log structured merge tree
* optimized for fast writes 
* writes batched in memory
  * Eventually flushed to disk (SSTable) at some point 
* **SSTable is sorted string table**
  * sorted based on key value of what we are storing
  * can leverage binary search
* In Cassandra each SSTable is 100mbs, but to scale we have more SSTables
  * SSTable are immutable, cannot be overrwritten and deleted

To optimize for writes

* When we overwrite, we just write a new entry to another SSTable
* When we dont need an SSTTable we just mark as deleted but does still exist on disk

### Replication

Benefit is Scale, Fault, Tolerance

One issue with Replication is **consistency**

Consider the **CAP** theorem here

* If there is a partition in the system (replication)
* If one node gets put to one node, but not another node yet. If a read where to happen on the wrong node, the data is not consistent.

* We can lock the node with the stale data down, but that will impact availability

In our case we favour partition tolenence and latency

* So we favor PA and give up C

#### Leaderless Repliaction approach

Optimized for writes, but has issues with consistency 

#### Quroum

The amount of nodes in our system that are agreeing to take an action, before the update is consider **accepted**

##### Write Qurom

If we have 3 machine `n=3` 

We can enforce rule such as `w=1` where one machine need to have a write before it is accepted

We can enforce rules such `w=3`, where all three machines need to have a write before it is accepted

`w=1` is low consistency

`w=3` is low avaiaiblity (because high latency), but strong/high consistency


##### Read Qurom

`r=1` at least one machine agree to the value that is ready

`r=3` wait for all 3 machines to agree on the value


##### Tunable Consistency

Cassandra allows you to configure `w=` to let you tune what you need

### Partioning

**Horiztiona Partioning:** Split it out to different machines (nodes)

**Vertical Partioning** Lesson common
Idea is to split columns to a different machine for  faster query

#### Sharding

Shard key to detemine how we break up our split/data in different machines/nodes/partitions

System should be edynamic to increase of decrease the number of partations

#### Consistency Hasing

Increase and Decreate the number of partations can be handled with Consistent hasing

Minimizne the amount of data we need to move when we inc/dec number of partitions


Imagine a ring, with 360 spots

How do we split up 360 spots

> If we split the hash key space into 3 nodes we have
node a: 0-120
node b: 120-240
node c: 240-360

**One problem is that**
if 120-240 goes down
then all the write will now gogo to 240-360

To address this problem is that we can have **virtual nodes**
just more arbitrarily spliting up the more hash key space to the number of nodes we have

instead we jave node a: 1-40, 120-160, 240-280


### Node Failure

#### How do we detect is a name goes down

Centralized approach

* Industry solution is **zookeeper**
  * Heart beat solution
  * Centrailzed control plane that handles node failures (rediret traffic to another node)

Divide the work approach

* Cassandra solution is **gossip** protocol
  * Each nodes gets an identifier
  * Each node checks heartbeat information of a few adjacment nodes and passes that information
  * Eventually the health status gets propagates to all nodes
    * Eventually a few nodes will know about the node that has no heartbeat for a while

#### How do we recovery

Hinted handoff

* If node A goes down, another node B accepts the writes until node A goes back up
* The write on another node gets flushed back to node A

### Concurrent Writes

If we dont have isolation with writes, we have to figure out how to deal with conlficts since we don't have prebuilt locking


#### Last write wins

Last value is most uptodate (uses clock)

#### Vector Clock

A vector clock is used  to track the logical ordering of events across multiple nodes without relying on a centralized clock. 

It consists of an array of counters, one for each node in the system, and is used to capture causal relationships between events, enabling detection of conflicts and concurrent operations in distributed environments.


