/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
  let totalNumWaysToReachTop = 1;

  function climb(stairLevel = 0) {
      // either climb 1 or 2
      // each level, increment stair level accordingly
      // if has reached n, increment totalNumWaysToReachTop
      if (stairLevel === n) {
          totalNumWaysToReachTop += 1;
          return;
      } else if (stairLevel > n) return;

      climb(stairLevel += 1);
      climb(stairLevel += 2);
  }

  climb();
  return totalNumWaysToReachTop;
};