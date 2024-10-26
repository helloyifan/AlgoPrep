# Design a Distributed Message Queue

## Fucntional Requirments

1. Fanout
   * One one Publisher / Producer can have multiple Consumer/Subscribers
2. Retain messages until delivered
3. At least once delivery (only do this)
4. Exactly once delivery (dropping this from reqs becaue it complicated)

## Non Functional

1. Scalable
   * Horizontally scalled
2. Persistent Storage
3. Throughput (high)


## High Level Design

### At Least once delivery

1. Publishers ->  Publish Forwarders -> Database

* Publish Forwarders would also acknolwedgement (ACK) with Publisher to confirm the message is stored (fault tolerance)
* Typically dones with HTTP, also consideration with security

1. Database -> Subscriber Forwarders -> Subscriber

* Once the message is stroed subscriber forwards can start reading message and Writes to Subscribers
* Once a message has been read with the relevent subscribers (ACK)
* Then we can remove the message from stroage

### Topic / Subscriptions - Fanout

* Can store different business requirement in different topics
* Messages are published by topics
* Messages are received by subscriptions
  * one subscription can get the messages of multiple topics
  * multiple subscribers can receive message for the same subscription


### Database Design

Since we don't need to do complex joins, we can likely use NoSQL
   * Relational would be another solution if we want to use ACID
      * Leverage Isolation since we have multiple forwarders
Key design: id_timestamp
Body: JSON we are storing

### Additional Retention

Keep messages for 7 days

Replication messaages between different data centers

### Considerations for Latency vs Fault Tolerance

When it comes to replication

Question:
Do we want to send ack, to publisher after its wriitten to one database or only send ack after it has been replicated once

Trade off
Latency: if we wait for replication
Fault Tolerence is less ideal if we dont wait


### Pull vs Push based delivery

* Pull Delivery:  subscribers checks for content at set cadence
   * if theres no messages then then its alot of wasted processing
   * benefit is requested can process data when it sends requests
   * this is better for batch processing

* Push Delivery: Subscriber forwarder pushes to subscriber asap
   * waits for Ack from subscriber to mark as messaged pushed
   * downside is that we might overwhelm subscribers
   * downside is wasted processing is subscriber is not ready for messages
   * upside is better latency
