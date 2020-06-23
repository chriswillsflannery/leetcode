/*
 * write a function that takes a string of text and returns true if
 * the parentheses are balanced and false otherwise. //done
 *
 * Example:
 *   balancedParens('(');  // false
 *   balancedParens('()'); // true
 *   balancedParens(')(');  // false
 *   balancedParens('(())');  // true
 *
 * Step 2:
 *   make your solution work for all types of brackets //done
 *
 * Example:
 *  balancedParens('[](){}'); // true
 *  balancedParens('[({})]');   // true
 *  balancedParens('[(]{)}'); // false
 *
 * Step 3:
 * ignore non-bracket characters
 * balancedParens(' var wow  = { yo: thisIsAwesome() }'); // true
 * balancedParens(' var hubble = function() { telescopes.awesome();'); // false
 *
 *
*/

// step 1

function isBalanced(string) {
  // for each left bracket there come after it, at some point, a right bracket
  const stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '(') {
      stack.push('(');
    } else {
      stack.pop();
    }
  }

  return !stack.length;
}

// console.log(isBalanced('('));  // false
// console.log(isBalanced('()')); // true
// console.log(isBalanced(')('));  // false
// console.log(isBalanced('(())'));  // true

// step 2

function isBalancedAllTypes(string) {
  const stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '(' || string[i] === '[' || string[i] === '{') {
      stack.push(string[i]);
    }
    if (string[i] === ')' && stack[stack.length - 1] === '(') {
      stack.pop();
    } else if (string[i] === ']' && stack[stack.length - 1] === '[') {
      stack.pop();
    } else if (string[i] === '}' && stack[stack.length - 1] === '{') {
      stack.pop();
    }
  }

  return !stack.length;
}

// console.log(isBalancedAllTypes('[](){}')); // true
// console.log(isBalancedAllTypes('[({})]'));   // true
// console.log(isBalancedAllTypes('[(]{)}')); // false
console.log(isBalancedAllTypes(' var wow  = { yo: thisIsAwesome() }')); // true
console.log(isBalancedAllTypes(' var hubble = function() { telescopes.awesome();')); // false