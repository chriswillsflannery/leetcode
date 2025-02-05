# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # no need to actualy merge arrays
        # binary search on both halves

        # use smaller array first
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums
        
        m, n = len(nums1), len(nums2)
        total_length = m + n
        half_total_length = (total_length + 1) // 2 # 2

        left, right = 0, m # search range for nums 1 # 0,2

        while left <= right:
            partition1 = (left + right) // 2 #mid point in nums1
            partition2 = half_total_length - partition1 # calculated point in nums2

            # get values around partition points
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            # check if we found correct partition
            if left1 <= right2 and left2 <= right1:
                # found correct partition, calculate median
                if total_length % 2 == 0:
                    # even length, avg of max of lefts and min of rights
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    # odd length, max of lefts
                    return max(left1, left2)
            # not found, adjust binary search
            elif left1 > right2:
                #too far right in nums1
                right = partition1 - 1
            else:
                #too far left in nums1
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted")

"""
ex
a [1,3,6,8]
b [2,5,6,9]

if these were sorted merged we would have:
[1,2,3,5,6,6,8,9]
median: 5.5


so we know we need 4 elements on the left side
and we need 4 elements on the right side
then median will be max of left side + min of right side  / 2
left [1,2,3,5]
right [6,6,8,9]
max of left 5
min of right 6
div by 2 we get 5.5

try putting partition here in nums1 [1,3|6,8]
then partition here in nums2 [2,5|6,9]

now check
left values [1,3] and [2,5]
right values [6,8] and [6,9]

max of all left values is 5
min of all right values is 6

is this correct?
do we have 4 elements on each side? YES
are all left values smaller than right values? YES
median = 5.5

-----

What if we had an invalid partition?

a [1,2,6|8]
b [2|5,6,9]

lefts [1,3,6,2]
rights [8,5,6,9]

problem: 6 in lefts is > 5 in rights
this tells us our partition in a is too far to the right
we need to move partition in a to the left

next we would try:

a [1|3,6,8]
b [2,5,6|9] # partiotion in b is automatically determined based on a
# because both sides must be balanced (8+1)/2

lefts [1,2,5,6]
rights [3,6,8,9]

6 in lefts is greater than 3 in rights - partition too far right in b
move partition left in b

a [1,3|6,8]
b [2,5|6,9]

"""
        