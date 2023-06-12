package findnumberinlist

func NumInList(list []int, num int) bool {
	// if list is nil return false
	// if list is empty return false

	// iterate each value of list
	for el := range list {
		// if target is found return true
		if el == num {
			return true
		}
	}
	return false
}

// NumInList([]int{1,2,3,4,5},5) // true
// NumInList([]int{3,3,3,3,3}, 5) // false
// NumInList(nil, 5) // false
// NumInList([]int{}, 5) // false
