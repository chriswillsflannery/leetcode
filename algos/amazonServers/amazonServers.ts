/*

Developers at amazon have their applications deployed on N servers. initially, the i-th server has an
id server[i] and can handle server[i] requests at a time.

For maintenance puirposes, some servers are replaced periodically. On a j-th day, all the servers with 
id equal to replaceId[j] are replaced with servers with id newId[j] that can serve newId[j] requests.
The total number of requests served on the jth day is the sum of the ids of the servers that the application
is running on.

Given server, replaceId, and newId, find the total number of requests served by the servers each day.
Note- the indices i and j are assumed to follow 1-based indexing.

ex.
n = 2, server = [20, 10], replaceId = [10, 20], newId = [20, 1]
day servers replacement newservers  totalrequests
1 [20, 10]  10=>20  [20,20] 20+20=40
2 [20,20]   20=>1   [1,1]   1+1=2

answer is [40, 2]

*/

function getTotalRequests(server, replaceId, newId) {
  const totalRequests: number[] = [];
  const serverCounter = {};
  let totalRequestsSum = 0; // 40

  // init counter and totalRequestsSum
  for (let val of server) {
    if (serverCounter[val] === undefined) {
      serverCounter[val] = 1;
    } else {
      serverCounter[val] += 1;
    }
    totalRequestsSum += val;
  }

  // iterate each day
  for (let j = 0; j < replaceId.length; j++) {
    // { 20: 2, 10: 1 }
    let replace = replaceId[j]; // 20
    let replaceWith = newId[j]; // 20

    if (serverCounter[replace] !== undefined) {
      let count = serverCounter[replace]; // 1
      totalRequestsSum += (replaceWith - replace) * count;

      if (replace === replaceWith) continue;

      if (serverCounter[replaceWith] === undefined) {
        serverCounter[replaceWith] = 1;
      } else {
        serverCounter[replaceWith] += 1;
      }

      if (serverCounter[replace] === 1) {
        delete serverCounter[replace];
      } else {
        serverCounter[replace] -= 1;
      }
    }

    totalRequests.push(totalRequestsSum);
  }

  return totalRequests;
}
