class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid):
            return 0

        rows, cols = len(grid), len(grid[0])
        
        maxIsle = 0
        coords = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()

        def dfs(r,c,size):
            visited.add((r,c))
            for [rOffset, cOffset] in coords:
                newR = r+rOffset
                newC = c+cOffset
                if (
                    0 <= newR < rows
                    and 0 <= newC < cols
                    and grid[newR][newC] == 1
                    and (newR, newC) not in visited
                ):
                    return dfs(newR, newC, size+1)
            return size

        for i in range(rows):
            for j in range(cols):
                print(grid[i][j])
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxIsle = max(maxIsle, dfs(i,j,1))
        
        return maxIsle