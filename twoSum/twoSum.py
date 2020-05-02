'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(list, target):
  dict = {}
  for num in list:
    if num in dict:
      return [dict[num], list.index(num)]
    else:
      dict[target - num] = list.index(num)

myNums = [2, 7, 11, 15]
print(twoSum(myNums, 9)) # expect [0,1]