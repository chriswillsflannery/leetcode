package matrix

func isValidCell(m int, n int, x int, y int) bool {
	return x >= 0 && x < m && y >= 0 && y < n
}

type Tuple struct {
	Values [2]int
	Number int
}

type NumTuple struct{ x, y int }

func updateMatrix(mat [][]int) [][]int {
	m, n := len(mat), len(mat[0])
	newMatrix := make([][]int, m)
	for i := range newMatrix {
		newMatrix[i] = make([]int, n)
	}

	q := []Tuple{}
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 0 {
				q = append(q, Tuple{Values: [2]int{i, j}, Number: 0})
				newMatrix[i][j] = 0
			} else {
				newMatrix[i][j] = -1
			}
		}
	}

	for len(q) > 0 {
		queueditem := q[0]
		q = q[1:]

		x, y := queueditem.Values[0], queueditem.Values[1]
		steps := queueditem.Number

		for _, row := range directions {
			nextX := row[0] + x
			nextY := row[1] + y

			if isValidCell(m, n, nextX, nextY) && newMatrix[nextX][nextY] == -1 {
				newMatrix[nextX][nextY] = steps + 1
				q = append(q, Tuple{Values: [2]int{nextX, nextY}, Number: steps + 1})
			}
		}
	}

	return newMatrix
}