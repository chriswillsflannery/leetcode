/**
 Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 */
var isValid = function (s) {
  // create stack
  // for each char in s
  // if char is an opener, push onto stack
  // otherwise
  // if top element of stack is corresponding opener tag,
  // pop stack
  // at end if stack is empty return true else false

  if (s.length === 1) return false;

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char === '(') {
      stack.push(')');
    } else if (char === '{') {
      stack.push('}');
    } else if (char === "[") {
      stack.push(']');
    } else if (stack.length === 0 || stack.pop() !== char) {
      return false;
    }
  }

  return stack.length === 0;
};

console.log(isValid("()"))
console.log(isValid("()[]{}"))
console.log(isValid("(]"))
console.log(isValid("([)]")) // false