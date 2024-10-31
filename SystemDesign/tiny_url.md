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

## Hight Level Design

### Stroage

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

# Stoped aat 10mins