class Solution:
    def largestRectangleInHistogram(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i # we don't know if we can extend backwards yet
            while stack and stack[-1][1] > h:
                # check max rect we can create
                # check current height backwards
                # then pop 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights) - i))
        return maxArea