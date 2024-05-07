
const grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]

const grid2 = [
    [0,2]
]

// 0 = empty, 1= fresh orange, 2 = rotten orange
// time starts at 0. each minute, rotten orange will infect directly adjacent fresh oranges.
// takes total of 4 minutes to rot all fresh oranges. return this number.

// use BFS with queue
// starting at each rotten orange, infect each orange and return how long search took.

type Tuple = [number, number];

function orangesRotting(grid: number[][]): number {
  let timeElapsed = -1;
  const m = grid.length; // 1
  const n = grid[0].length; // 2
  // queue for rotten
  const q: Tuple[] = [];
  let numFresh = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      // append to rotten queue
      if (grid[i][j] === 2) {
        q.push([i,j]);
      } else if (grid[i][j] === 1) {
        numFresh += 1;
      }
    }
  }

  if (numFresh === 0) return 0;

  while (q.length) {
    timeElapsed += 1;
    for (const _ of q) {
      const layer = q.shift();
      if (!layer) continue;

      const [i, j] = layer;
      for (const [i_offset, j_offset] of [[0,1],[1,0],[-1,0],[0,-1]]) {
        const r = i + i_offset;
        const c = j + j_offset;
        if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] === 1) {
          grid[r][c] = 2;
          numFresh -= 1;
          q.push([r,c]);
        }
      }
    }
  }

  if (numFresh > 0) {
    return -1
  }


  return timeElapsed;
}