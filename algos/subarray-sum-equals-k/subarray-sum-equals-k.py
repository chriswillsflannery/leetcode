"""
given an array of ints and int k, return total number 
of contiguous subarrays whose sum equals k

ex1
input nums = [1,1,1] k=2
output= 2
reason: 1,1 (indeces 0,1) and 1,1 (indeces 1,2)
"""

from typing import List

class Solution:
    def subarray(self, nums: List[int], k: int) -> int:
        # build up array of prefixes
        # for each prefix, get difference between prefix and k
        # is there a breakpoint in the contiguous subarray such that we can 
        # make the prefix == k?

        # build up a hash of prefixSum to count 
        # this accounts for possibility of negative numbers

        # simultaneously build up list of prefixes
        # while we compute our result, so that we're only
        # removing prefixes which are part of the subarray
        #we've seen so far

        # make sure to include an empty prefixSum for 0

        # [magic implicit 0 prefix here] [1,-1,1,1,1,1] k = 3
        # for each value in the array, we say,
        # take the sum up to this point. subtract k from it.
        # we get a resulting value.
        # we say, how many times have we seen this resulting value before?
        # add that count to our result.
        # then we make sure that currentSum gets incremented
        # (we have now seen this currentSum 1 more time)

        #clarifying q's
        # why do we need the magic 0 again?


        res = 0
        currSum = 0

        prefixSums = { 0: 1 }

        for n in nums:
            currSum += n
            diff = currSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return res

    """
    overall rationale can be summed up like:
    we want to know how many different contiguous subarrays
    can sum up to k.

    we can get determine whether a subarray sums up to k
    by taking the total sum up to that point, eg
    [1,2,3,4,5] k = 12
         ^   ^
    here we want to know if 3,4,5 == k
    so we take the total sum up to that point (15):
    [1,3,6,10,15]

    and we say: ok , if I take 15 - k, which is 3:
    is there a total sum up to some point which === 3?
    and more specifically (since there is the possibility
    of having negative numbers,)
    how many total sums up to some point === 3?

    so we start off with an empty dict (account for magic 0)
    { 0: 1 }
    and an empty total sum: 0
    and an empty res: 0 (this will track how many subarrays total k)

    and we say: ok, first sum is 1. 1-k = -11.
    Have we seen -11 as a sum before (is it a key in dict?)
    no, it's not. ok, do nothing.
    add this sum to our dict. 
    dict is now { 0: 1, 1: 1 }

    ok, next sum is 3. 3-k = -9.
    Have we seen -9 as a sum before?
    no, it's not. Ok, do nothing.
    Add this sum to our dict.
    dict is now { 0: 1, 1:1, 3:1 }

    ok, next sum is 6. 6-k = -6
    Have we seen -6 as a sum before?
    no. do nothing.
    Add this sum to our dict.
    dict is now {0:1,1:1,3:1,6:1}

    ok, next sum is 10. 10-k = -2
    have we seen -2 as a sum before?
    no. do nothing.
    Add this sum to our dict.
    dict is now {0:1,1:1,3:1,6:1,10:1}

    ok, next sum is 15. 15-k = 3.
    Have we seen 3 as a sum before?
    Yes, we have, 1 time. Ok, add 1 to our res.
    add this sum to our dict.
     dict is now {0:1,1:1,3:1,6:1,10:1, 15:1}

    now we've reached end of list.
    res is 1.
    Therefore, there is 1 contiguous subarray here
    which == 12, that is, [3,4,5]
    """
