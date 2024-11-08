# Google Maps

## Functional

Navigate from source to desination

* should give a reaonably good route
    * should be the best we can givebased on the information we have
* user location tracking
* ETA, based on traffaic data

- Assume we have map data (something on the order of 5TBs)
    - all roads and map is 5 TBs


## Non Functional
- 1B Dau, scale
- Accuracy
- Availability , reliability
- Latency tolerated
    - Its okay to take a few seconds to generate the route


## High Level Design


### Spacial Indexing Concept

Querying spatial data like maps as quick as possible
- Spatial indexing (break up the world into squares)
- Think of the earth is y and x (2d)

How do we store it a relation database
* we could index the word with x and y cooridnates
* well does that make sense? how many decimals of percision do we want to go?

#### Tiles / Spactial indexing
lets break up the world into squares
    - We can also break up world into squares recursively

- This is a pretty common datastructures
    - This datastrucuture is used in
    - **Quadtree**
    - And **geohashing** (slighly differenet)
        - **Geohashing** is 00,01,10,11 to represent the 4 quadrants
        - Next level is 0000, 0001, 0010, 0011 etc...

- We can map the Physical address of ou world to this spacial index
    - or maping long/lat to spacial index
    - since its a map we have very fast lookup time

- Cities can be represented as nodes in a graph
- **But to index nodes of the graph, we are using a spacial index like quadtress/geohashin**


### Routing
- With the nodes on a graph, we can run shortest path djiskta algorithm to figure out the route
    - We dont need to load the entrie map of earth to run this algorithm
    - **we can just have this starting tile and load neighboring tiles**
        - dijkstras uses BFS


### Services and stuff

Note google maps has an offline mode, basically once you have route all you need is GPS signal to figure out where you are

#### Route Services

- **Focus of this interview**
- Route Service -> cache -> GraphDB
- Cache on common generated routes (or sub routes)
- We can shard GraphDB 
    - on first digits of our geohash (example 0010)
        - in sharded database, it’s generally more efficient to keep operations within a single shard when possible
        - one downside is that if you route from Country 1 to Country 2, then we might go accross shards which is less efficient but acceptable
    - Alternativly, each tile could have all the route information
        - Store all route information for tile in NoSQL and use Quadtress to finds the key which can be used to instantly find the document
        - each tile have to fit in a document
        - each tile would reference all its neighbouring tiles
        - We can index this nosql table with inmemory quadtree in memory


#### Location Sevice

- Traffic information
- Historical information
    - Used NoSQl database to log historial data, how much traffic does each road have at reach hours
    - NoSqL has large amount of data
- Use Kafka or Kineses to store the aggregated version of this information in another DB to represent **traffic data**

##### Traffic Data

- Can be used to set weights on the graph that is used to set route



## Details

### How do we model Location data of user?

- userId, timestamp, long/lat 
- For real time updates from user to server
    - we can leverage websockets for real time updates  and listen for realtime updates (updates to routes or whatever)

### What are we doing with the src/dst information of the Route
- Where do we render the picture? (map data)
- The map is just an image
- We can leverage a content delivery system to efficient deliver it to the user
- We can store it in object storage
- We can index the images by geohashing again
