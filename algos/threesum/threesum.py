# unsorted list. return any set of 3 numbers which add up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort first so numbers are in ascending order

        for i in range(len(nums)): # leftmost pointer
            if i > 0 and nums[i] == nums[i-1]: #where there is a duplicate number, ignore it
                continue

            j, k = i+1, len(nums)-1 # left and right

            while j < k: 
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]]) # add trips
                    j += 1 # increment left ptr, there still may be more trips using this "i"

                    while nums[j] == nums[j-1]: # ignore duplicates on left ptr
                        j += 1
        return res