# Twitter

## Funcitonal

1. Follow Others
2. Create Tweets
3. View Feed

### Assuming interviewer providded the following

Tweet length: 140 character (each character is a byte so 140B)

* Lets assume its 1KB due to metadata
* Its also possible there could be media attached, maybe assume theres 1 MB in total per tweet
* Media not stored in db, bttw just for reference

## Non Funcitonal

500 m users
200 m DAU

Average user reads 100 tweets a day

* Daily 20 b reads

20 b reads x 1MB per tweed

* 20 b * 1000 is 20 t
* 20 t * 1000 is 20 p (so we have 20 petabytes of read data daily)

* Eventually consistent is fine
* Some users have no followers, some have millions

## High Level Design

Bottlenecked by getting the news feed

* Horizontally scaled and put load balancer infront of it

### Datastore

We have a read heavy db

* Typically we choose nosql for read heavy systems
* noSQL is easier to scale

#### Relational Database

* We have to do joins because we have a **relational model**
* We have the concept of "**following**"
* To address scale we have "sharding"

#### Another thing to consider

* leverage graphDB
* storage non relational data in noSQL


#### Caching

* Since we have massive reads we **must have caching**


#### Media stored in Object storage

* CDN, distribute static content in CDN to bring it closer to users
  * **CDN is always push vs pull** algorithms
  * We want a pull based CDN, since we only bring it closer to users when they want to see it


## Detail Design

### APIs

> createTweet(text, media, userId)

> getFeed(userId)

* HTTP headeer auth token prevents one person from using another persons userId

>follow(userId, followPersonUserId)

### Tables

#### Tweets

- Timestamp
- Media (refence to object storage meedia)

#### Follow:

* Followee (being followed)
* Follower

In a database, records should be grouped by follower, such that we can use a **range query** to quickly get all of the followee for a user to generate feed


## Scaling DB

### Reads

* We have so many reads
* To scale DB we can leverage REad only replicas


### Writes

If we have 50M reads, there is 100k seconds a day thats 500 writes per second, not account for peak

To scale writes we use **sharding**

* Shard the Follow table
  * We want to shard on userId to keep user on the shard exist on, using other shards would making sharding reduandant

### Caching

Help us lower latency by caching popular tweets

Bottle neck is exists in different partitions / shards of of Tweet tables


### Async Generating news feeds

Generating for 200 M DAU isnt too expensive


#### Pub/Sub

Pub/Sub queue to send work to a worker cluster

* Send output to "feed cache"
  
**Problem with approach**
One problem is that, we cant possibly Update all of the feeds generate by the pub/sub when a popular user sends a new tweet

This is a trade off, we must leverage both fetching some components of feed at loading and some async

Business logic for this pending