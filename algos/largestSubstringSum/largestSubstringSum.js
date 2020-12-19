/**
 * given an array of numbers, return the largest sum of any substring of the numbers,
 * 
 * for example:
 * [1,2,3,4,5] -> 15
 * [1,2,0,3,4] -> 10
 * [1,2,-5,3,4] -> 7
 * [100, -200, 300, -200, 400]; -> 500
 */

const ss1 = [1,2,3,4,5]
const ss2 = [1,2,0,3,4] 
const ss3 = [1,2,-5,3,4]
const ec1 = [100, -200, 300, -200, 400];

 /**
  * 
  * @param {number[]} array 
  * @returns {number} 
  */
function largestSubString(array) {
  let totalSub = 0;
  let largestSoFar = 0;

  array.forEach(cur => {
    if (largestSoFar > totalSub) totalSub = largestSoFar;
    if (cur >= (cur + largestSoFar)) {
      largestSoFar = cur;
    } else if (cur < (cur + largestSoFar)) {
      largestSoFar = cur + largestSoFar;
    }
  });
  return Math.max(totalSub, largestSoFar);
}

console.log(largestSubString(ss1)) // 15
console.log(largestSubString(ss2)) // 10
console.log(largestSubString(ss3)) // 7

// edge cases?

console.log(largestSubString(ec1));