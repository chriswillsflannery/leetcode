# given a list of non-negative integers nums,
# arrange them such that they form the largest number and return it

# the result may be large, so return a string
# input: [10,2]
# output: '210'

# ex 2
# input: [3,30,34,5,9]
# output: "9534330"

"""
greedy approach
take largest 1st number as 1st
for example, 9 comes before 34 because 9 > 3

compare between any 2 digits
which is larger [9, 34]
934? or 349?
convert ints to strings,
append them together,
convert back to ints and compare?

"""

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

            def compare(n1, n2):
                if n1 + n2 > n2 + n1:
                    return -1
                else:
                    return 1

            nums = sorted(nums, key=cmp_to_key(compare))

            # edge case: [0,0,0] -> "0"


            return str(int("".join(nums)))
            