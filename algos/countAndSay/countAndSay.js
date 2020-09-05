// count and say - recursive

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n, newString = "1") {
  if (n === 1) return newString;
  // convert n to string
  let value = newString[0]; // 1
  let occurencesOfValue = 0; // 1
  // loop over string and cache number of occurences of each current number until a new number is viewed, at that point, paste into new string (.repeat()) number of current number
  let newNew = "";
  for (let i = 0; i < newString.length; i++) {
    if (newString[i] === value) {
      occurencesOfValue += 1;
    } else {
      newNew += occurencesOfValue;
      newNew += value;
      value = newString[i];
      occurencesOfValue = 1;
    }
  }
  newNew += occurencesOfValue;
  newNew += value;
  return countAndSay(n - 1, newNew);
};
