package twopointersortwosum2

type Tuple struct{ int1, int2 int }

func twoSum2(target int, nums []int) Tuple {
	ptr1ind := 0
	ptr2Ind := len(nums) - 1

	for ptr1ind <= ptr2Ind {
		ptr1 := nums[ptr1ind]
		ptr2 := nums[ptr2Ind]

		if ptr1+ptr2 < target {
			ptr1 += 1
		} else if ptr1+ptr2 > target {
			ptr2 -= 1
		}

		if ptr1+ptr2 == target {
			return Tuple{ptr1, ptr2}
		}
	}

	return Tuple{-1, -1}
}