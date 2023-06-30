func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	mapp := make(map[rune]int)

	for _, v := range s {
		mapp[v]++
	}
	for _, v := range t {
		mapp[v]--
	}
	for _, v := range mapp {
		if v != 0 {
			return false
		}
	}
	return true
}