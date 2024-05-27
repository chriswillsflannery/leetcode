// return all sets of triplets such that n[i] !== n[j] !== n[k]
// and that n[i] + n[j] + n[k] == 0

/**
 * Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


*/

package main

import (
	"fmt"
	"sort"
)

// approach - sort ascending first
// [-1,0,1,2,-1,-4] becomes [-4, -1, -1, 0, 1, 2]
// start with index 0, say this is k, k = -4
// then do 2 ptr approach at either end
// i = -1, j = 2
// get sum. -4 -1 + 2 = -3. This is too small, so we should
// attempt moving i up 1 index. k=-4, i=-1, j=2. sum=-3
// still too small. move i again.k=-4, i=0,j=2. sum=-2
// if a sum of 0 is reached, return [k,i,j]
// do this for each value of k in array

func threesum(nums []int) [][]int {
	results := [][]int{}
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {

		//check to prevent repeats
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		target := nums[i]
		left := i + 1
		right := len(nums) - 1

		for left < right {
			sum := nums[left] + nums[right] + target

			if sum == 0 {
				results = append(results, []int{target, nums[left], nums[right]})
				left++
				right--

				//check to avoid duplicates
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				for left < right && nums[right] == nums[right+1] {
					right--
				}
			} else if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			}
		}
	}
	return results
}

func main() {
	ints := []int{-1, 0, 1, 2, -1, -4}
	fmt.Print(threesum(ints))
}
