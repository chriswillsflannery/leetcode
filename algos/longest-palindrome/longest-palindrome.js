function isEven(num) {
  return num % 2 === 0;
}

/**
* @param {string} s
* @return {number}
*/
var longestPalindrome = function(s) {
  const ofOccurencesS = {};
  for (let i = 0; i < s.length; i++) {
      ofOccurencesS[s[i]] ? 
          ofOccurencesS[s[i]] += 1
          : ofOccurencesS[s[i]] = 1;
  }
  let total = 0;
  for (let key in ofOccurencesS) {
      let val = ofOccurencesS[key];
      if (isEven(val)) total += val;
  }

  return total + 1;
};