class Solution {
  pacificAtlantic(heights) {
    const ROWS = heights.length;
    const COLS = heights[0].length;
    const pacific = new Set();
    const atlantic = new Set();

    for (let i = 0; i < ROWS; i++) {
      this.dfs(i, 0, pacific, heights[i][0], ROWS, COLS, heights);
      this.dfs(
        i,
        COLS - 1,
        atlantic,
        heights[i][COLS - 1],
        ROWS,
        COLS,
        heights
      );
    }

    for (let j = 0; j < COLS; j++) {
      this.dfs(0, j, pacific, heights[0][j], ROWS, COLS, heights);
      this.dfs(
        ROWS - 1,
        j,
        atlantic,
        heights[ROWS - 1][j],
        ROWS,
        COLS,
        heights
      );
    }

    const res = [];
    for (let i = 0; i < ROWS; i++) {
      for (let j = 0; j < COLS; j++) {
        const coord = i * COLS + j; // generate unique val
        if (pacific.has(coord) && atlantic.has(coord)) {
          res.push([i, j]);
        }
      }
    }
    return res;
  }

  dfs(r, c, visited, prevHeight, ROWS, COLS, heights) {
    const coord = r * COLS + c; // generate unique val
    if (
      r < 0 ||
      c < 0 ||
      r == ROWS ||
      c == COLS ||
      heights[r][c] < prevHeight ||
      visited.has(coord)
    )
      return;

    visited.add(coord);
    this.dfs(r + 1, c, visited, heights[r][c], ROWS, COLS, heights);
    this.dfs(r - 1, c, visited, heights[r][c], ROWS, COLS, heights);
    this.dfs(r, c + 1, visited, heights[r][c], ROWS, COLS, heights);
    this.dfs(r, c - 1, visited, heights[r][c], ROWS, COLS, heights);
  }
}
