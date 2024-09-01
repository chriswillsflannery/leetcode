import collections

# // BFS solution
# neetcode
class Solution(object):
    def numIslandsBFS(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in directions:
                    shfitedR = r + dr
                    shiftedC = c + dc
                    if (shfitedR in range(rows) and
                        shiftedC in range(cols) and
                        grid[shfitedR][shiftedC] == "1" and
                        (shfitedR, shiftedC) not in visited):
                        q.append((shfitedR, shiftedC))
                        visited.add((shfitedR, shiftedC))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
    

    # DFS solution
    # https://www.youtube.com/watch?v=__98uL6wst8
    def numIslandsDFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return 0
        coords = [[0,1],[1,0],[-1,0],[0,-1]]
        NoOfIsland = 0

        def dfs(r, c):
            for cR, cC in coords:
                offsetR = r + cR
                offsetC = c + cC
                if (0<=offsetR<rows and
                    0<=offsetC<cols and
                    grid[offsetR][offsetC] == "1"):
                    grid[offsetR][offsetC] = "2"
                    dfs(offsetR, offsetC)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    NoOfIsland += 1
                    dfs(r, c)
        return NoOfIsland

