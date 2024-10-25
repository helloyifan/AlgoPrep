# Youtube

## Functional

Upload Video

Watch Video

## Non Functional Requirements

Reliability
* videos should be stored and wont disappear

Scale
* 1 Billion DAU
* Can assume each user watches 5 videos a day
* Can assume thata 1 video is uploaded for 100 videos watched
  
So 5 billions views daily
5 billion / 100 is 50 million videos uploaded daily

Top 5% of videos account for 90% of the views

We favor Availability > Consistency
    * so in Cap theore we favor A over C
    * Consistency is not super imporatnt for watiling to watch videos
    * Avaiability means no outage

We need no latency


## High Level Design

### User journey
 
App Server (with LB in front of it considerations)
    * User stored in Object storage 
      * Preferred for media storage

Object storage handels Replication (using object storage satifies out reliability considerations)
    * We also need to store metadata (such as titles and refernce to object store)
      * Need table for Videos (metadata)
      * Need table for User (metadata)

NOSQL database (joins less efficient)
* This is just a choice we made for this question, not too many justification
* NoSQL database becaue we have to handle such a high volume of daata
  * NoSQL are easier to scale horizontally with less considerations architecural planing and operational overhead 
* We can have data denormalized (denormalized means storing redundant data to avoid costly joins)
* Having data denormalized will offer better performance and the trade off is stale redundant data thats stored
* Example is maybe updating profile pictures has eventual consistency if we store it in multiple places and rely on jobs to syncronize

Queue

* As raw video files are stored in Object storage, we queue jobs to encode the video files (handle in another server)

Encoding app server

* Encoded video stored in another object storage
* Uploading raw enables youtube to control the compression for optimal delivery

> if we have 50 million  videos a day and theres roughly 100k seconds day, that means we need to processed 500 encode 500 videos a second
> we also are assuming it take 60 seconds to encode a video which isnt super accurate

> Well how many workers do we need?
> Naively, 500 videos a second each video takes 60 seconds to enchode, so 30k workers would be a number thats logically derived (to keep up wit the load)

CDN

* The encoded video file will be loaded from the CDN which is pulled from the encoded object stroage

Cache to app server

* Add cache to app server as since 90% of views go to 5% of videos,
* Caching would be a great way to improve performance here


## Improvements to design

ill just use `>` to denote them above

### Additional Notes

When we watch a video, we dont need to load the whole video (so its buffered)

But people also skip around in a video, and when you skip in a video it updates the buffer

**Videos are not streamed, we used HTTP to load chunks of the video**
* We load chunks of video in webm in HTTP requests
* This is a technique to **lower latency**

Another knit, youtube storeds video chunks in browser memory
* client side code need to be good to free memory


### UDP and TCP

UDP favors streaming 
* for streaming a sports game youd want udp
* udp risks dropping chunks of the video, but thats okay aslong as its fast and fresh

TCP is handshakes (reliablity, but higher latency)
* but with a video thats stored somewhere and you want to see all parts of thevideo
* TCP favours reliability
* We can use HTTP with TCP


### Rate Limiting
We can handle this load balance

### 