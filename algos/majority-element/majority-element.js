/**
 * @param {number[]} nums
 * @return {number}
 */
 var majorityElement = function(nums) {
  let maj = {
      el: nums[0],
      occ: 1,
  };
  const map = {};
  nums.forEach((num) => {
      map[num] ? map[num] += 1 : map[num] = 1;
      if (map[num] > maj.occ) {
          maj.el = num;
          maj.occ = map[num];
      }
  });

  return maj.el;
};


// alt
// /**
//  * @param {number[]} nums
//  * @return {number}
//  */
//  var majorityElement = function(nums) {
//   let res = 0;
//   let majority = 0;
  
//   for (let n of nums) {
//       if (majority === 0) {
//           res = n;
//       }
      
//       majority += n === res ? 1 : -1;
//   }
  
//   return res;    
// };