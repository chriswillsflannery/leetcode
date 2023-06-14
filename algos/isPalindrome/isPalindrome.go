// dum dum way

import (
	"fmt"
	"regexp"
	"strings"
)

func reverseString(str string) string {
	// Convert the string to a rune slice
	runes := []rune(str)

	// Get the length of the rune slice
	length := len(runes)

	// Swap characters in-place to reverse the string
	for i, j := 0, length-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	// Convert the rune slice back to a string
	reversed := string(runes)

	return reversed
}

func isPalindrome(s string) bool {
	// const alteredString = s.replace(/[^a-zA-Z0-9]/g, "");

	// Compile the regex pattern
	regex := regexp.MustCompile(`[^a-zA-Z0-9]`)

	// Remove non-alphanumeric characters
	result := regex.ReplaceAllString(s, "")

	reversed := reverseString(result)

	lowerResult := strings.ToLower(result)
	lowerReversed := strings.ToLower(reversed)

	fmt.Println(reversed)

	return lowerResult == lowerReversed
}

// smarty pants way 2 pointer

func isPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		// skip any non alphanumerics
		for i < j && !(unicode.IsLetter(rune(s[i])) || unicode.IsDigit(rune(s[i]))) {
			i++
		}
		for i < j && !(unicode.IsLetter(rune(s[j])) || unicode.IsDigit(rune(s[j]))) {
			j--
		}
		// finds match, ie. "r" and "r" in "racecar"
		if i == j {
			break
		}
		// bail early if non match i.e. "r" and "d" in "railroad"
		if unicode.ToLower(rune(s[i])) != unicode.ToLower(rune(s[j])) {
			return false
		}
	}
	return true
}

