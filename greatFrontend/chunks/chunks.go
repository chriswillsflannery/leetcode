/*
Implement a function chunk(array, [size=1]) that splits the input array
into groups of length size and returns them within a new array.
If array can't be split evenly, the final chunk will be the remaining
elements. The function should not modify the original input array.
*/

package main

import "fmt"

func chunk(array []int, size int) [][]int {
	chunks := [][]int{}

	chunk := []int{}
	for number := range array {
		if len(chunk) == size {
			chunks = append(chunks, chunk)
			chunk = []int{}
		}
		chunk = append(chunk, number)
	}

	chunks = append(chunks, chunk)

	return chunks
}

func main() {
	res := chunk([]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}, 3)
	fmt.Print(res)
}