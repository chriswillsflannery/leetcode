"""
You are shopping on Amazon.com for some bags of rice. Each listing displays the number of grains of rice that the bag contains.
You want to buy a perfect set of rice bags from the entire search results list, riceBags. A perfect set of rice bags, perfect, is defined as:
• The set contains at least two bags of rice.
* When the rice bags in the set perfect are sorted in increasing order by grain count, it satisfies the condition
perfect[i] * perfect[i] = perfect[i+1] for all 1 ≤ i < n.
Here n is the size of the set and perfect[i] is the number of rice grains in bag i.

Find the largest possible set perfect and return an integer, the size of that set. If no such set is possible, then return -1. It is guaranteed that all elements in riceBags are distinct. 

Complete the function maxSetSize in the editor.
maxSetSize has the following parameter:
    int riceBags[n]: the list of bags of rice by rice grain counts
Returns
int: the size of the largest set possible or -1 if there is none 

Example 1:

Input:  riceBags = [625, 4, 2, 5, 25]
Output: 3 
Explanation:

All of the possible perfect sets:

- [625, 25] # 25 * 25 = 625
- [4, 2] # 2 * 2 = 4
- [5, 25] # 5 * 5 = 25
- [625, 5, 25] 5 * 5 = 25, 25 * 25 = 625
The largest perfect set has size 3.

"""

# from typing import List

# def func(arr: List[int]) -> int:
#     n = len(arr)
#     max_length = 0
#     for i in range(n):
#         cur = arr[i]
#         tmp = [cur,]
#         while cur**2 in arr:
#             tmp.append(cur**2)
#             cur = cur**2
#         if len(tmp) > 1:
#             max_length = max(max_length, len(tmp))

#     return max_length

# riceBags = [625, 4, 2, 5, 25]
# print(riceBags, "output:", func(riceBags))

# riceBags = [3, 9, 4, 2, 16]
# print(riceBags, "output:", func(riceBags))


# riceBags = [3, 9, 4, 2, 16, 256]
# print(riceBags, "output:", func(riceBags))

# this operation will run in O(n) * O(log(n)) * O(n) = O(n^2 * log(n)) due to the nested loops. yeesh

# from typing import List

# def optimized_func(arr: List[int]) -> int:
#     rice_set = set(arr)
#     max_length = 0
    
#     for num in arr:
#         # for each number, we check if its square root is in the set.
#         # this prevents us from starting a sequence where there actually is an earlier
#         # number to use as the start of a sequence, and saves us a cycle.
#         if num ** 0.5 not in rice_set:  # Check if this could be the start of a sequence
#             current = num
#             length = 1
#             while current ** 2 in rice_set:
#                 current = current ** 2
#                 length += 1
#             max_length = max(max_length, length)
    
#     return max_length if max_length > 1 else -1  # Return -1 if no valid set found

# # Test cases
# test_cases = [
#     [625, 4, 2, 5, 25],
#     [3, 9, 4, 2, 16],
#     [3, 9, 4, 2, 16, 256],
# ]

# for riceBags in test_cases:
#     print(f"{riceBags} output: {optimized_func(riceBags)}")

# -- we can still optimize even further, by sorting in ascending order first.

from typing import List

def sorted_optimized(arr: List[int]) -> int:
    if len(arr) < 2:
        return -1
    
    arr.sort()
    rice_set = set(arr)
    max_length = 0

    for i, num in enumerate(arr):
        if max_length >= len(arr) - i:
            break # no chance of finding longer sequence

        if num ** 0.5 in rice_set:
            continue # this number is part of a sequqnce starting with a smaller number
        
        current = num
        length = 1
        while current ** 2 in rice_set:
            current = current ** 2
            length += 1
        max_length = max(max_length, length)

    return max_length if max_length > 1 else -1

# Test cases
test_cases = [
    [625, 4, 2, 5, 25],
    [3, 9, 4, 2, 16],
    [3, 9, 4, 2, 16, 256],
    list(range(1, 1000001))  # Large test case
]

for riceBags in test_cases:
    print(f"{riceBags[:5]}{'...' if len(riceBags) > 5 else ''} output: {sorted_optimized(riceBags)}")