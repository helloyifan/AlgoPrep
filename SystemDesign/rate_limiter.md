# Design a Rate Limiter

## Functional questions

After we designing for a "backend api"?
Does it protect a microservice?
    * lets assume its able to protect many microservices

How do we identify users?
    * Do we use user-id, do they have to sign up?
    * Ratelimiter should be general enough
        * should use many ids, uid, or IP even (which is more unique)

## NonFunctional requirement

Most important
* Latency, it should not slow things down (1mms)
* Throughput (we should be able to add more resources and it should still work at higher load)
* Stroage 
  * We would need to support different Rules YT rules, google search rate limiting rules (but thats limited)
  * number of users
    * each user takes the following room
      * each IP can store a certain number of requests
      * if a IP is 4 bytes and lets assume each payload is 128 bytes, so in total each user takes 132 bytes
      * if we have 1 billion users, we have 132 billion bytes aka 132 GB
      * 132GB is feasisable to fit into memory
  * Availability (great to talk about)
    * **Fail - Open**
      * If this fails, its just rate limiter doesnt work, but service does
    * **Failed - closed**
      * Nothing else works if rate limiter goes down

## High level design
    * When clients call us, it first hits our rate limiter service,, this service acts like a reverse proxy
    * we can store rules in a DB, NoSQl, SQL doesnt matter as much as this isnt high volume
      * [BottleNeck] latency: Reading from DB is slower is then reading from memeory, we can put a cache infront of it, and since we dotnt have alot of rules we can just periodically update the cache from db
    * We can use a in memory key value store to store the Rate limiting (fast access)
      * [BottleNeck] volume: If we have TPs of memory, we can share the inmemory key value store
      * we can leverage consistent hashing
  
## Details
* What type of algorithm do we use for rate limiting.
* Suppose we have a rule of 100 request per min
  * What does that mean: one simple algorithm is that for every minute we allow for 100 request, and when the next clock minute starts we allow for another 100 request
    * This is called **"Fixed Window"** Algoritm
    * But this opens up for an exploit of 1:59 sends 100 requests and 2:00 sends 100 requests
      * This is a problem, but might not a huge problem
  * A better algorithm is **"Sliding Window"**
    * Down side is we need to store the exact timestamp of each request
    * Each time stamp is 4 bytes , so 100 requests if 400 bytes per user
    * The large the limit size the more space it takes
  * Theres many more alogrithms here, but dont worry to much about domain knowledge
    * Others that exist could be Token Bucker, Slidnig Window Count

## Data Schema

Rule:

id: string
api: string
operation: string
timeUnit: enum (second, minute, hour)
numOfRequestAllowed: int
