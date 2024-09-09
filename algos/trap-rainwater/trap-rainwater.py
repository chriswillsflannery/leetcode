# You are given an integer array heights where heights[i] represents the height of the ithith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not len(heights) or len(heights) == 1:
            return 0
        
        maxSoFar = 0
        left, right = 0, len(heights) - 1

        while left < right:
            minheight = min(heights[left], heights[right])
            diff = right - left
            localarea = minheight * diff
            maxSoFar = max(maxSoFar, localarea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxSoFar