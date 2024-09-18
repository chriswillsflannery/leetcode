import collections
from typing import List

# given an m x n grid, each cell can be;
# 0 representing an empty cell
# 1 representing a fresh orange
# 2 representing a rotten orange

"""
every minute, any fresh orange that is 4-directionally adjacent
to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no
cell has a fresh orange. If it is impossible, return -1
"""

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Approach:
        create visited grid
        BFS starting at 2
        counter tracks # of rounds
        each round, iterate over grid and rot adjacents
        only if fresh
        if no adjacents to rot, return counter
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m,n = len(grid), len(grid[0])

        visited = grid
        q = collections.deque()
        countFreshOrange = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2: # rotten
                    q.append((i, j))
                if visited[i][j] == 1: # fresh
                    countFreshOrange += 1
        # there are no fresh oranges to rot
        if countFreshOrange == 0:
            return 0
        # there were no rotten oranges added to queue
        if not q:
            return -1
        
        minutes = -1
        dirs = [(1,0), (0,1), (-1, 0), (0,-1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        countFreshOrange -= 1
                        q.append((i,j))
            minutes += 1
        if countFreshOrange == 0:
            return minutes
        return -1
    
    """
    start by identifying all spaces which have rotten oranges.
    add those to queue.
    identify all fresh oranges and total them.
    work through queue. Each time through queue, increase time.
    For each item in queue, rot all adjacent items.
    Newly rotted items get added to queue.
    Newly rotten items get subtracted from fresh count.
    Each new "Layer" of rotten items goes into queue.
    Total # of times through queue = total minutes.

    If queue gets emptied completely and fresh count still > 0
    we can't rot all items (some unreachable)
    """ 
