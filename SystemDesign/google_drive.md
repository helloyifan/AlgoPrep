# Google Drive

## Functional

Upload

Download

Remove

Folders

## Non Functionall

Total users: 200 M users

Dau: 50M

Every user gets 15GB of free stroage

Obviously there a subset of superusers

* Not targeting devs, so unlikely there will be  petabytes of users
* Can assume most users will get 15gb of data and wont use it all

200,000,000 and 15 GB means

3,000 PB of data which is 3 Exabyte (aka just alot of storage)

One thing to think about is reliability

* we need replication of all the data (maybe stored in 3 places around the world)

Assuming the average person saves 2 files a day

* 2 files /day 10 MB each
* Read / write ration is 2:1

We don't really care about

* Throughput (probably wont be spam up loading)
* Latency (its okay to wait a few seconds)

We do really want

* **High Availability**
* **High Reliaibility**

## High Level Design

### Data Model

#### Metadata

* Can go in SQL or NoSQL database
* Choose NoSQl,
  * we just need a key value store
  * no need to consider stuff like joins
  *

#### Files

* Need to be persistent

##### Sol 1. Hadoop Distributed file System (HDFS)

<https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs>

Pros:

* Data is stored in a tree like structure
* Stored in hierarchy, (which is helpful because we have folders as req)
* Can edit files in File system

Cons

* Scaling this file system, this is less scaalble
* We can use a distirbued file system, but its complicated

#### Sol 2. Object Store (Assuming its chosen)

Technically a flat datastrucutre

* Folders are S3 are an illusion

Pros:

* Scaiability comes for free
  * given my S3

Cons:

* You cannot edit files in Object store (only delete and create)
  * Note this isnt a requirement so maybe its okay

### Design Architecture

Load Balancer

App Server

Object Store

KV store

Cache (optional but weak)

* How often would we even use it

### Design Details

* Worth mentioning configure permissions for Object Storage
  * Since we want to restrict access to only our own app servers
* If we only use S3 for object storage, it will be too expensive
  * We should leverage **Block Level Storage**

#### Block Level Storage
  
* When user uploads a pieces of data
  * we break it up in 4mb chunks, we store these 4 chunks
  * When user Reads, we reassembled the file from metadata

Pros:

* **Deduplication**
  * if we ever, noticed a **duplicated 4mb block**
  * we **do not need to restore this data**
  * We can do this on a global level saves alot of money

Cons:

* Managing deletes are complicated
  * We can't delete a block unless its not referenced by any file
  * maybe we can keep track of a **counter of how many files use a block**

Implementation -**Data Blocks**-  Content Addressable Storage

* If we can **generate a unique id** for each block
  * If we every **generate the same id**, we know it already exists 
* This is called **Content Addressable Storage**

If we create hash based on the content,

* Then how do we edit a file
* If you update a block, does it mess up someones elses file

Failed Upload

* If the files fails upload half way through, well thats fine since we are breaking it up to 4mb chunks, we can pick up where we left off

## Folders

Folders exists as metadata in KV store

* Each Folder has reference to each child file a user storage
* Each Folder is owned by user
* File has reference to datablocks
* Each file and folder have two way points to parent and child

## Deletion (optimization to save space)

* Focus on deleting file from KV store
* To delete file from object store
  * Async data collection service that scans through KV store to see if a datablock is no longer being used


## Reliability

What happens when a load balancer goes down?

* Redirect to another load balancer
* How do we know it goes down? HeartBeat, or Zookeeper