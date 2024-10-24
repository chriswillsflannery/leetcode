class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        approach:
        BFS from every cell adjacent to pacific
        BFS from every cell adjacent to atlantic

        can recursively move to a cell with higher or same value
        if any 2 cells from BOTH BFS converge, record convergent cell
        """
        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        # prevHeight lets us check if we are allowed to visit this cell
        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or 
            r < 0 or c < 0 or r == ROWS or c == COLS or
            heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for c in range(COLS):
            # go through every pos in first row (touching pacific)
            dfs(0, c, pacific, heights[0][c])
            # go through every pos in last row (touching atlantic)
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            # go through every pos in first col (touching pacific)
            dfs(r, 0, pacific, heights[r][0])
            # go through every pos in last col (touching atlantic)
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
        return res
