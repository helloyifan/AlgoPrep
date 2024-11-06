# Design Tiny Url

## Functional Requirement

Long url to tiny url 8 characters

Might be a +1 requirement:
    User can delete url if they own it
    we need ownership model

By default url expires after 1 year

What whould happen if multiple users have the same long url

Good clarifying question

* If u made the same tiny url for the same long url as someone else
  * then what happens when it expires for you 
  * Does the other persons url also expire?
  * [Sol] even for the same long url, its still unique short url

## Non functional req

Fault Tolernt

* If component fail, the whole thing should fail

Latency

* if long lateny to use short url, then you might as well not use it

Write to Read ratio

A bit arbitrary

But maybe we can assume a 1:100 ratio

### How many urls are we going to create?

Lets assume its 1 b per month

* If we have 8 characters will we run out space
  * Alpha numeric is 62 = a-zA-Z0-9
  * 62^8 which is the realm of Trillion
  * if we use 1 b per month and we have trillion then its 1000months so we are good


1 b month is 33 m per day

100k seconds in a day

33m/100k = 300 tps for writes
300 * 100 = 30,000 tps for reads


### Storage

1 b writes
each cheracter is a Byte, so we are storing 8gb

But we might also need metadata, so per url lets assume we have alot of metadata lets use 1kb of meta data

1kb of metadata * 1b of writes = 1 tb of information to store per month
* (which is reasonable)
* big but not too big

## High Level Design

### Stroage for URL DB

- `{uid, longURl, shortURL, expiration}`

#### NoSQL vs SQL

* We dont have super high writes, we have alot of reads
  * NoSQL not super needed for high scale writes
  * NoSQL does scale to handle reads
* We dont need acid rules
  * no need for atomic transactions
  * SQL not super needed
* No relational data, no need for bunch of joins or complexity query
  * SQL not needed
* Tolernt for eventual consistency
  * NoSQL works okay

Choice for DB is NoSQL


* Read heavy system
  * Caching layer (in memory cache)
    * a few tiny urls are use more frequently then the others
  * How big should our cache be?
    * 256gbs?
    * should we use sharding
  * Which Caching algorithm should we use?
    * Eviction polict
    * Least Frequencly Used
      * What if it was something trendy for a day that got 1t views, but after no1 cared
      * Less good
    * Least Recently Used
      * Only "active urls" in cache to minimize missed
  
## Status Codes

### 301 Moved Permanently

- This will tell browser to cache the location at which the resource exist (no need to hit our server)

### 302 Found (Temporary Redirect)

- This wont cache in browser

For our use case 301 makes for better peformace, but 302 can enable us to collect analytics

## Collisions / Key Generation

### Hashing

* Hashing, can't guarantee no colision
  * Two different strings could result in the same hash
  * Thats why this solution doesnt work
  
### Generate all Keys

* In a DB somewhere we store all possible keys
  * We could have a **KeyGenerator** service responsible for this
  * IF we are running out of keys we could make more
  
KeyGenerator Service could be called by other services for keys

* It could cache a subset of keys in keyGenerator service memory.

We want to avoid reusing keys, if a key is used we need to mark it as so in DB (mark it as USED)

* `{key: string, isUsed: boolean}`
* at expiry we can have the feature to make isUsed back to false

#### What if multiple UrlGenerator intances were using the same keys

* If we use a SQL database, we can use ACID
  * Atomic and Isolation property can help
  * Atomic: All of nothing
  * Isolation means: 1 by 1
* With a SQL database we can guarantee that UrlGenerator intances dont vend out the same keys

#### UrlGenerator Fault Tolerance

* What if we load keys into memory, and at that point we mark them as used
* And then the URL Generator instance crashes 

Trade off to discuss

* if we mark URL as used when we load to memory cache and mark as used when we load to cache
  * Pro: Better latency
  * Con: risk of loss
* if we read from DB everytime and mark as used 
  * Pro: Less risk of loss
  * Con: Worse latency

#### Locking

Better Solution would be to implement locking to prevent multi UrlGenerator from using the same set of keys

## Deletes and URL Expiry

### CleanUp service

Async, Reads from DB and filters by expiration date

* and removes them from URL DB
* also to make sure to update record in Keys DB

ASync means eventual consistency here, which is okay for our usecase

## Scale

Easiest way to scale would be to introduce load balancer infront of client and servers and replicas


### Partition

Hash user ID with Consistent hashing

#### Consistent Caching

* Each user is assigned to a particular partition
* So we always check there first
* Otherwise round robin

* But thats how we can split up data in our URL database