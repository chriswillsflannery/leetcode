# you're given a binary tree represented as an array like [3,6,2,6,-1,10] where -1 is a non-existent node.
# so in the top layer you have 3.
# to its left is 6 and to its right is 2.
# to the left of 6 is 9, and to the right is non-existent.
# to the left of 2 is 10, and to the right is non-existent.

# Write a function which determines whether the left or right branch of the tree is larger. the size of each branch is the sum of the node values. if the tree has 0 nodes or if the size of the branches are equal, return empty string.

def calculate_branch_sum(arr, index):
    if index >= len(arr) or arr[index] == -1:
        return 0
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    return arr[index] + calculate_branch_sum(arr, left_child_index) + calculate_branch_sum(arr, right_child_index)

def solution(arr):
    if not arr or arr[0] == -1:
        return ""
    
    left_child_index = 1
    right_child_index = 2
    
    left_sum = calculate_branch_sum(arr, left_child_index)
    right_sum = calculate_branch_sum(arr, right_child_index)
    
    if left_sum > right_sum:
        return "Left"
    elif right_sum > left_sum:
        return "Right"
    else:
        return ""
