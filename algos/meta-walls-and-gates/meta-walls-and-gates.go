package main

import (
	"fmt"
	"math"
)

type Tuple struct{ r, c int }
type Set map[Tuple]struct{}

func (s Set) Add(r, c int) {
	s[Tuple{r, c}] = struct{}{}
}

func (s Set) Remove(r, c int) {
	delete(s, Tuple{r, c})
}

func (s Set) Contains(r, c int) bool {
	_, found := s[Tuple{r, c}]
	return found
}

func wallsAndGates(rooms *[][]int) {
	rows := len(*rooms) // ptr.deref to access underlying slice
	cols := len((*rooms)[0])
	visit := make(Set)
	q := [][]int{}

	addRoom := func(q *[][]int, r int, c int, dist int) {
		if r < 0 || r == rows || c < 0 || c == cols || visit.Contains(r, c) || (*rooms)[r][c] == -1 {
			return
		}
		visit.Add(r, c)
		*q = append(*q, []int{r, c})
		(*rooms)[r][c] = dist
	}


	for i := range *rooms {
		for j := range (*rooms)[i] {
			if (*rooms)[i][j] == 0 {
				q = append(q, []int{i, j})
			}
		}
	}

	dist := 0
	for len(q) > 0 {
		for i := 0; i < len(q); i++ {
			layer := q[0]
			q = q[1:]

			r, c := layer[0], layer[1]
			(*rooms)[r][c] = dist

			addRoom(&q, r+1, c, dist+1)
			addRoom(&q, r-1, c, dist+1)
			addRoom(&q, r, c+1, dist+1)
			addRoom(&q, r, c-1, dist+1)
		}
		dist++
	}

}

func main() {
	emp := math.MaxInt64
	wal := -1
	gat := 0

	matrix := [][]int{
		{emp, wal, gat, emp},
		{emp, emp, emp, wal},
		{emp, wal, emp, wal},
		{gat, wal, emp, emp},
	}

	wallsAndGates(&matrix)

	for _, row := range matrix {
		fmt.Println(row)
	}

}
