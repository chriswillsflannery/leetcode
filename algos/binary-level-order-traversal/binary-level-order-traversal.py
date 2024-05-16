# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        level = 0
        levels = []

        self.bfs(root, level, levels)
        return levels

    def bfs(self, root: Optional[TreeNode], level: int, levels: List[List[int]]) -> None:
        if root is None:
            return None
        
        if len(levels) == level:
            levels.append([])
        
        levels[level].append(root.val)
        
        self.bfs(root.left, level+1, levels)
        self.bfs(root.right, level+1, levels)

        
        