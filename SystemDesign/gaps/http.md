# Network Protocol

A network protocol is a set of rules governing data communication between devices in a network.

## HTTP

- Purpose How message are formated for web browser and web servrs
- Layer 7 Application
- Stateless
- METHODS: GET, POST, PUT, DELETE

## TCP

- Purpose: Reliable ordered and error checked delivery of stream of bytes
- Layer 4 Transport layer
- Maintains connection between host


## HTTP status code

1xx - Informational:
    100 - Continue
    101 - Switching Protocols

2xx - Success:
    200 - OK (The request was successful)
    201 - Created
    204 - No Content

3xx - Redirection:
    301 - Moved Permanently
    302 - Found (Temporary Redirect)
    304 - Not Modified

4xx - Client Errors:
    400 - Bad Request
    401 - Unauthorized
    403 - Forbidden
    404 - Not Found
    405 - Method Not Allowed
    408 - Request Timeout
    429 - Too Many Requests

5xx - Server Errors:
    500 - Internal Server Error
    501 - Not Implemented
    502 - Bad Gateway
    503 - Service Unavailable
    504 - Gateway Timeout

## HTTP method strucuture

- `GET` do not have a body
  - basically everything after `/` is PATH
  - we use URL path and query parameters to retrieve data

### Breakdown

1. Request Line:
   - HTTP Method (GET, POST, PUT, DELETE, etc.)
   - Request URI (path)
   - HTTP Version

2. Headers:
   - Headers provide metadata and control information for HTTP requests and responses.
   - Authorization (credentials)
   - Content type
   - Cookie
   - Cache control
   - Origin: Cors request

3. Empty Line:
   - Seperate headers from the body

```
GET /path/to/resource HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

[Message body would go here for methods like POST, but GET typically doesn't have a body]

```