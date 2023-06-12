var closingToOpening = map[byte]byte{
	')': '(',
	'}': '{',
	']': '[',
}

func isValid(str string) bool {
	// create stack
	// loop ever char in string
	// if char is opening brace push opposite onto stack
	// else if stack is empty or popped element is not current char return false

	// if stack is empty return true

	s := []byte(str)
	stack := make([]byte, 0)

	for _, ch := range s {
		matchingOpening, isClosing := closingToOpening[ch]

		if !isClosing {
			stack = append(stack, ch)
			continue
		}

		if len(stack) == 0 {
			return false
		}

		lastOpening := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if lastOpening != matchingOpening {
			return false
		}
	}

	return len(stack) == 0
}