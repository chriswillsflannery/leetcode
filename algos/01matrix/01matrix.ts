// given an mxn matrix return the nearest 0 for each cell
// similar to rotting oranges

const matrix = [
  [0, 0, 0],
  [0, 1, 0],
  [1, 1, 1],
];
const expected = [
  [0, 0, 0],
  [0, 1, 0],
  [1, 2, 1],
];

// starting at every 0, BFS and replace with distance observed

const isValidCell = (m: number, n: number, x: number, y: number) => {
    return x >= 0 && x < m && y >= 0 && y < n;
}

function updateMatrix(mat: number[][]): number[][] {
  const m = mat.length;
  const n = mat[0].length;
  const newMatrix: number[][] = Array.from(new Array(m), () => new Array(n));
  const q: [[number, number], number][] = [];
  const directions: number[][] = [[0,1],[1,0],[0,-1],[-1,0]];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (mat[i][j] === 0) {
        q.push([[i, j], 0]);
        newMatrix[i][j] = 0;
      } else {
        newMatrix[i][j] = -1;
      }
    }
  }

  while (q.length) {
    const queuedItem = q.shift();
    if (!queuedItem) continue;

    const [[x, y], steps] = queuedItem;

    for (const [x_offset, y_offset] of directions) {
        const nextX = x + x_offset;
        const nextY = y + y_offset;

        if (isValidCell(m,n,nextX,nextY) && newMatrix[nextX][nextY] === -1) {
            newMatrix[nextX][nextY] = steps + 1;
            q.push([[nextX, nextY], steps + 1]);
        }
    }
  }

  return newMatrix;
}
