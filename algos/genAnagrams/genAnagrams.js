/**
 * Given a single input string, write a function that produces all possible anagrams
 * of a string and outputs them as an array. At first, don't worry about
 * repeated strings.  What time complexity is your solution?
 *
 * Extra credit: Deduplicate your return array without using uniq().
 */

/**
  * example:
  * var result = anagrams('abc');
  * console.log(result); // [ 'abc', 'acb', 'bac', 'bca', 'cab', 'cba' ]
  */

const genAnagrams = (str, res = []) => {

  const perm = (curStr, memo = '') => {
    if (memo.length === str.length) {
      res.push(memo);
      return;
    }
    for (let i = 0; i < curStr.length; i++) {
      let current = curStr[i];
      let others = curStr.slice(0, i) + curStr.slice(i + 1);
      memo += current;
      perm(others, memo);
      memo = memo.slice(0, memo.length - 1);
    }
  }

  perm(str);
  return res;

};

console.log(genAnagrams('abc'));