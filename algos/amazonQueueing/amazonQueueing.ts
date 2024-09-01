/*

Amazon web services is a cloud computing platform with multiple servers. One of the servers is assigned 
to serve customer requests. There are n customer requests placed sequentially in a queue, where the i-th
request has a maximum waiting time denoted by wait[i]. That is, if the i-th request is not served within
wait[i] seconds, then the request expires and it is removed from the queue.
The server processes the requests following FIFO principle. The 1st request is processed first, and the nth
request is processed last. At each second, the first request in the queue is processed. At the next second,
the processed request and any expired requests are removed from the queue.

Given the maximum waiting time for each request denoted by the array wait, find the number of requests 
present in teh queue at each second until it is empty.

Note: 
if a request is served at some time instant t, it will be counted for that instant and is removed from the
next instant.
The first request is processed at time 0. A request expires without being processed when time = wait[i]. It
must be processed while time < wait[i]. See the example below.
The initial queue represents all requests at time = 0 in the order they must be processed.

Example
n = 4, wait = [2,2,3,1]

time 0: 1st request served. num requests in queue is 4. queue = [1,2,3,4]
time 1: requeset 1 removed. Request 4 removed (wait[3] = 1) because time=wait[3]=1 which exceeds the
max waiting time. Also, request 2 is served. The number of requests in the queue at time=1 seconds is 2.
queue = [2,3].
time 2: request 2 is removed as processed. request 3 is served. number of requests in queue is 1. queue = [3]
time 3: request 3 is removed as processed. Number of requests in queue is 0. queue = [empty]

answer: [4,2,1,0]
(number of requests in the queue at each instant until queue becomes empty)

*/

/*
 * Complete the 'findRequestsInQueue' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY wait as parameter.
 */

function findRequestsInQueue(wait) {
  // Write your code here
}

// import heapq

// def findRequestsInQueue(wait):
//     heap = []
//     res = [0] * len(wait)

//     # Add everything to the heap
//     for ticket in wait:
//         heapq.heappush(heap, ticket)

//     for i in range(len(wait)):
//         while heap and heap[0] <= i:
//             heapq.heappop(heap)
//         res[i] = len(heap)
//         if wait[i] in heap:
//             heap.remove(wait[i])

//     return res

// wait = [2, 2, 3, 1]
// print(findRequestsInQueue(wait))
