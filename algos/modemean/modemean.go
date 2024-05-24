// Given an array of numbers, determine if the mode and mean of the array are equivalent

//  Caveats:
//  Math.floor the mean
//  If there are multiple modes, use the max of the modes
//  Return true or false

package main

import (
	"fmt"
	"math"
)

func mean(n []int) int {
	sum := 0
	for num := range n {
		sum += num
	}
	divided := sum / len(n)
	return int(math.Floor(float64(divided)))
}

func mode(n []int) int {
	hash := make(map[int]int)
	for num := range n {
		if num, ok := hash[num]; ok {
			hash[num] += 1
		} else {
			hash[num] = 1
		}
	}

	maxMode := n[0]
	maxModeValue := 1

	for mode, modeval := range hash {
		if mode > maxMode && modeval >= maxModeValue {
			maxMode = mode
			maxModeValue = modeval
		}
	}

	return maxMode
}

func modeMean(n []int) bool {
	if len(n) == 0 {
		return false
	}
	if len(n) == 1 {
		return true
	}
	return mode(n) == mean(n)
}

func main() {
	fmt.Print(modeMean([]int{1, 2, 2, 3, 3, 4, 5}))
}

// console.log(modeMean([1, 2, 2, 3, 3, 4, 5])); // mode 3. mean 2. false
// console.log(modeMean([1, 2, 2, 3, 3, 4, 6])); // mode 3. mean 3. true
// console.log(modeMean([6, 4, 3, 3, 2, 2, 1])); // true
