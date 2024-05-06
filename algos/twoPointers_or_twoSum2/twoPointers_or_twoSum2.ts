// given a target and a sorted array, find the two nums which equal the target
// it is not guaranteed that there will be two nums which sum to target.

const target = 18;
const nums = [2, 11, 7, 15];

function twoSum2(target: number, nums: number[]): [number, number] {
  let ptr1Ind = 0
  let ptr2Ind = nums.length - 1;

  while (ptr1Ind <= ptr2Ind) {
    let ptr1 = nums[ptr1Ind]
    let ptr2 = nums[ptr2Ind]

    if (ptr1 + ptr2 < target) {
      ptr1Ind += 1;
    } else if (ptr1 + ptr2 > target) {
      ptr2Ind -= 1;
    }

    if (ptr1 + ptr2 === target) {
      return [ptr1, ptr2];
    }
  }

  return [-1, -1]
}

console.log(twoSum2(target, nums));