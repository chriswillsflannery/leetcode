/**
given a 2d array like the following:

[
    [1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0]
]

where 1 represents a piece of gravel and 0 represents an empty space.
I want it to use a 2d array to represent a flower pot.
its important to make sure that whenever you water your plant any water that doesn't get absorbed by the roots drains to the bottom of the pot.

I need the function to return whether there is a route of 0's
from the top row, which reaches the bottom row, contiguous,
only moving up, right, left or down (not diagonal)

*/

const fillFlowerPot = (pot: number[][]): boolean => {
  // early return any corner cases
  if (!pot.length || !pot[0].length) return false;

  const m = pot.length;
  const n = pot[0].length;
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];
  const q: number[][] = [];

  // fill queue initially with any 00's in first row
  for (let j = 0; j < n; j++) {
    if (pot[0][j] === 0) {
      q.push([0, j]);
      // mark any already viewed 0's as visited
      pot[0][j] === 2;
    }
  }

  while (q.length > 0) {
    const layer = q.shift();
    if (!layer) continue;

    const [i, j] = layer;
    for (const [i_offset, j_offset] of directions) {
      const r = i + i_offset;
      const c = j + j_offset;
      // make sure offsetted value is in-bounds
      if (r >= 0 && r < m && c >= 0 && c < n && pot[r][c] === 0) {
        q.push([0, j]);
        // mark any already viewed 0's as visited
        pot[0][j] === 2;
      }
    }
  }

  // if any element in last row has been converted into a 2, water flows out
  if (pot[pot.length - 1].some((el) => el === 2)) {
    return true;
  } else {
    return false;
  }
};
