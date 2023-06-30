func search(nums []int, target int) int {
	// using sort package
	// i := sort.SearchInts(nums, target)

	// if (i < len(nums) && nums[i] == target) {
	//     return i
	// }
	// return -1

	lo := 0
	hi := len(nums) - 1

	for lo <= hi {
		mid := lo + (hi-lo)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}