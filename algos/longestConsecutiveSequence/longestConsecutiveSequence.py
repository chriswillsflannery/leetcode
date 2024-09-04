# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # look at entire sequence and figure out which numbers
        # do not have a left neighbor

        # convert list to set
        # for each num in set, check if left nieghtor exists in set

        # if it DOES have a left neighbor, skip it - 
        #this number is not the start of a sequence

        # each leftmost num is the start of a sequence
        # for each start of sequence, check if it has a right neighbor
        # continue until reaching end of sequence
        # calculate total length for this sequqnce
        # compare it against longest length we've seen so far
        seq = set(nums)
        longest = 0

        for num in seq:
            if num-1 not in seq:
                length = 1
                while (num + length) in seq:
                    length += 1
                longest = max(length, longest)
        # return seqs with greatest len
        return longest


