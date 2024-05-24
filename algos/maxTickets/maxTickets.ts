/**
Consider an array of n ticket prices, tickets. A number, m, is defined as the size of some
subsequence of tickets, s, where each element
covers an unbroken range of integers. That is, if the elements in s are sorted, the absolute
difference between any elements j and j + 1 is
either 0 or 1. Determine the maximum length of a subsequence chosen from the tickets array.

Example
tickets = [8, 5, 4, 8, 4]
Valid subsequences, sorted, are {4, 4, 5} and {8, 8}. These subsequences have m values of 3 and 2, respectively. Return 3.

Function Description
Complete the function maxTickets in the editor below.
maxTickets has the following parameter(s):
int tickets[n]: the ticket prices

Returns
int: the maximum possible value of m

Constraints
1 ≤ n ≤ 105
1 ≤ tickets[i] ≤ 109

 */

function maxTickets(tickets: number[]) {
  if (tickets.length === 0) return 0;
  if (tickets.length === 1) return 1;
  // track max M seen so far
  let maxMSeenSoFar = 0;

  // track local subsequence as array
  let localSubsequence: number[] = [];

  // sort array ascending
  tickets.sort((a, b) => a - b);
  // insert first element in local subsequence
  localSubsequence.push(tickets[0]);

  // for each tick in tickets starting at elem 1
  // if tick same as or 1 greater than last element in local subsequence add to local subsequence
  // else
  // find max between current MaxM and localSubsequence length, and replace maxM
  // empty current local subsequence and add tick to local subsequence
  for (let ticket of tickets) {
    const lastInSub = localSubsequence[localSubsequence.length - 1];
    if (ticket === lastInSub || ticket - 1 === lastInSub) {
      localSubsequence.push(ticket);
    } else {
      maxMSeenSoFar = Math.max(maxMSeenSoFar, localSubsequence.length);
      localSubsequence = [ticket];
    }
  }

  return maxMSeenSoFar;
}
