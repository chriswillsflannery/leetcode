/*

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

*/

const myinput = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
];

/*

memo = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
];

*/

const minPathSum = function (grid) {
  const numRows = grid.length; // 3
  const numCols = grid[0].length; // 3
  const memo = [];

  for (let i = 0; i < numRows; i++) {
    memo[i] = new Array(numCols).fill(0);
  }

  return minPathSumHelper(grid, numRows - 1, numCols - 1, memo);
};

function minPathSumHelper(grid, row, col, memo) { // row: -1, col: 2
  if (row === 0 && col === 0) return grid[0][0];
  if (row < 0 || col < 0) return Number.MAX_SAFE_INTEGER;
  if (memo[row][col] !== 0) return memo[row][col];

  const res = Math.min(minPathSumHelper(grid, row - 1, col, memo), minPathSumHelper(grid, row, col - 1, memo)) + grid[row][col];
  console.log('res', memo, row, col, res);
  memo[row][col] = res

  return res
}

console.log(minPathSum(myinput));