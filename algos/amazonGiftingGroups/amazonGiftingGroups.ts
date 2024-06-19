/*

Audible Gifting Groups
At audible, a subscriber can gift an audiobook from his/her library to any other non-subscriber to
kick start their audiobook journey. The first time subscriber can receive up to a max of N audiobooks
from their friends/relatives. When a non-subscriber receives an audiobook, we can infer that the two
may be related. Similarly, if the non-subscriber receives gifted books from two other subscribers,
we can infer that all of them are related and the three of them form a group. More formally, a group
is composed of all of the people who knew one another, whether directly or transitively. AUdible would
like your help finding out the number of such distinct groups from the input data.

Example: consider the following input matrix M:
[1,1,0]
[1,1,0]
[0,0,1]
Every row corresponds to a subscriber and the value M[i][j] determines if j was gifted a book by i.
In the above example, user 0 has gifted a book to user 1 and so they are connected [0][1], while
person 2 has not received a book from anyone or gifted book to anyone. therefore there are two groups

Determine the number of groups represented in a matrix.

*/

// input [ '1100', '1110', '0110', '0001' ]

function countGroups(related) {
  // Write your code here
  console.log(related);
}
