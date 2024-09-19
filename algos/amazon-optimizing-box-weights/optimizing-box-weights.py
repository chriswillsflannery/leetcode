"""
An amazon fulfillment associate has a set of items that need to be
packed into two boxes. Given an integer array of the item weights
to be packed, divide the item weights into two subsets, A and B,
for packing into the associated boxes.

Respsect the following:
1. the intersection of A and B is null.
2. The union of A and B is equal to the original array.
3. The number of elements in subset A is minimal.
4. The sum of A's weights is grteater than the sum of B's weights.

Example:
n=5
arr = [3,7,5,6,2]
A satisfied by [5,7] and [6,7]
"""

def minimalHeaviestSetA(arr):
    arr.sort(reverse=True)
    # [7,6,5,3,2]

    # initialize sums for A and B
    total_sum = sum(arr)
    A_sum = 0
    A = []

    # select elements for A until its sum is greater than B's sum
    for item in arr:
        A_sum += item
        A.append(item)
        if A_sum > total_sum - A_sum:
            break
    
    #return subset A in increasing order