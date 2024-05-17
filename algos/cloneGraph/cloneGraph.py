
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# return a deep clone of graph.

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        oldToNew = {}
        # could implement as stack or queue, doesn;t really matter
        # implements like { oldNode: newNode }
        stack = [node]

        while stack:
            cur = stack.pop()
            if cur not in oldToNew:
                clone = Node(cur.val)
                oldToNew[cur] = clone
            else:
                clone = oldToNew[cur]
            
            for neighbor in cur.neighbors:
                if neighbor not in oldToNew:
                    stack.append(neighbor)
                    newNeighbor = Node(neighbor.val)
                    oldToNew[neighbor] = newNeighbor
                clone.neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]
        