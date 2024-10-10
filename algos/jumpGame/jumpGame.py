class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution (O(n))
        """
        starting with the goal, see if we can 
        work our way backwards to first indx

        each time we move leftward, if we find a 
        space which can reach the goal, we can move
        the new goalpost to that space

        to determine whether a space can reach
        the current goal, we take that space index
        plus the max value it can jump

        if we reach index 0, return true
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
