// return all sets of triplets such that n[i] !== n[j] !== n[k]
// and that n[i] + n[j] + n[k] == 0

/**
 * Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


 */

// approach - sort first in ascending order
// 3 ptrs
// for each number (ptr1), get left ptr (number immediately to right) and right ptr (number at end of array)
// if sum === 0 keep
// if sum too low move left ptr 1 space to right
// if sum too high move right ptr 1 space to left

function threeSum(nums: number[]): number[][] {
  nums.sort((a,b) => a-b)

  const arrays = []
  const map = {}

  for (let i = 0; i < nums.length - 2; i++) {
      // skip duplicates
      if (i > 0 && nums[i] === nums[i-1]) continue;
      let left = i + 1, right = nums.length - 1;

      while (left < right) {
          const sum = nums[i] + nums[left] + nums[right];
          if (sum === 0) {
              const result = JSON.stringify([nums[i], nums[left], nums[right]])
              if (!(result in map)) map[result] = 1
              left++
          } else if (sum < 0) {
              left++ 
          } else {
              right--
          }
      }
  }
  return Object.keys(map).map(item => JSON.parse(item))
};