# Discord

## Funcitonal Requirements

- Servers
  - channels
    - picking up where you left off (focus is here)
- Messages in channels
  - should see messages show up when sent

- Mentions numbers
  - visual indidcator for channel

## Non functional Requirements

- Minmize latency (most important)
  - latency makes this unusable
- High Availability 
- 5 million daily active users
- 50 million messages sent a day
- 20k memembers in a server as a limit
- Max messagessize is 2kb
- ANother observation is most messages are writtern and read once
- So only the last 100 messages are used

## Hgiht Level Message

### APIs

#### sendMessage(body)

- parameters:
  - server
  - channel

Typically sent with HTTP request

#### receivingMessage()

- polling(1s) with HTTP calls
  - probably wouldnt be very effective, you dont get a new message every 1 second
  - if you increase 5s polling theres latency
- websockets
  - when theres a new message sent to the server. the server will push it to the client with websocket
- as an alternative to websockets, theres also HTTP streaming 

#### viewing a channel
##### viewchannel()
- parmaeters
  - channel
  - paginate token to see the lack 10 messages
    - when the last messsage they saw 
    - maybe this could be a timestamp
    - we can query the message from a certain channel from a certain time range

client -> server -> Db


### Database considerations

SQL - because this is low scale (premise of the question)

#### Tables

`Messages`

- id: string
- uid: string
- mentionid: string # which user did we mention to calculate the mentions number
- serverId: string
- channelId: string # we will use this to shard our db
- send_at: Date # index based on this because we will need message from a certain timerange


> sharing is to break a table up
> indexing: is ordering
    - todo, what does index really mean

`UserActivity`

- id: string
- uid: string
- serverid: string
- channelId: string
- last_read_at: Date # we will use this to know when the last message this user read (last read time)

#### here is the query that will be executed on channel load

```sql
SELECT *
FROM Messages="example"
AND sent_at >
    (select last_read_at
    FROM UserActivity
    WHERE uid = "jonathan")
```

#### here is the query that will be executed for mention count

- We cant run the same query as above, because its just as slow
as getting the messages
- Plus we have to do it N times for N channels

We can make this better with a in memory cache

- When a message is sent to the server
- If there is a mentionId, the server will send a request to the server keep track of channel mentions count in the cache
- Server and client connections is handled with websocket
