# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Brute force:
        For each node, get longest path on left, and longest path on right.
        Then calculate sum of two paths.

        DFS on left and right.
        Keep track of "height" of left and right while traversing.
        Add heights of left and right, and compare against max height.
        """

        if root is None:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        

"""
DFS
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # returns height
        def dfs(root):
            # need this here...
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            #...to signify here that we are updating res outside of scope
            res = max(res, left + right)

            return 1 + max(left, right)
        dfs(root) # we don't care about return val here
        return res

