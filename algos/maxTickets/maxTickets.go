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
 package main

import (
	"fmt"
	"sort"
)

func maxTickets(n []int) int {
	if len(n) == 0 {
		return 0
	}
	if len(n) == 1 {
		return 1
	}

	maxM := 0

	localSubsequence := []int{}

	sort.Ints(n)

	localSubsequence = append(localSubsequence, n[0])

	for i := 1; i < len(n); i++ {
		ticket := n[i]
		lastElem := localSubsequence[len(localSubsequence)-1]
		if ticket == lastElem || ticket-1 == lastElem {
			localSubsequence = append(localSubsequence, ticket)
		} else {
			maxM = max(maxM, len(localSubsequence))
			localSubsequence = []int{ticket}
		}
	}

	return maxM

}

func main() {
	fmt.Println("Hello, 世界")
	tickets := []int{8, 5, 4, 8, 4}
	maxval := maxTickets(tickets)
	fmt.Print(maxval)
}
