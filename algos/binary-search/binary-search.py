class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        approach:
        guess in middle of list
        if guess is to small, make new list
        starting from middle to end
        if guess too large, make new list
        starting from start to middle
        """

        L, R = 0, len(nums) - 1

        while L <= R:
            M = L + ((R - L) // 2) # // shorthand to floor val
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            else:
                return M
        return -1
