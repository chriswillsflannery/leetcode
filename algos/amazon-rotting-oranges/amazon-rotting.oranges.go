package amazonrottingoranges

// 0 = empty, 1= fresh orange, 2 = rotten orange
// time starts at 0. each minute, rotten orange will infect directly adjacent fresh oranges.
// takes total of 4 minutes to rot all fresh oranges. return this number.

// use BFS with queue
// starting at each rotten orange, infect each orange and return how long search took.

func orangesRotting(grid [][]int) int {
	timeElapsed := -1
	m, n := len(grid), len(grid[0])
	// queue for rotten
	q := [][]int{}
	numFresh := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			// append to rotten queue
			if grid[i][j] == 2 {
				q = append(q, []int{i,j})
			} else if grid[i][j] == 1 {
				numFresh += 1
			}
		}
	}

	if numFresh == 0 {
		return 0
	}

	for len(q) > 0 {
		timeElapsed += 1
		for i := 0; i < len(q); i++ {
			layer := q[0]
			q = q[1:]

			i, j := layer[0], layer[1]
			offsets := [][]int{{0,1},{1,0},{0,-1},{-1,0}}

			for _, row := range(offsets) {
				i_offset, j_offset := row[0], row[1]
				r, c := i+i_offset, j+j_offset
				if r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1 {
					grid[r][c] = 2
					numFresh -= 1
					q = append(q, []int{r, c})
				}
			}
		}
	}
	if numFresh > 0 {
		return -1
	}

	return timeElapsed
}
