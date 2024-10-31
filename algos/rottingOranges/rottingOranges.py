class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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
        ROWS, COLS = len(grid), len(grid[0])

        rottingQ = collections.deque()
        fresh = 0
        minsElapsed = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rottingQ.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        coords = [[0,1],[0,-1],[1,0],[-1,0]]
        while fresh > 0 and rottingQ:
            for i in range(len(rottingQ)):
                r,c = rottingQ.popleft()
                for dr, dc in coords:
                    rOffset, cOffset = r + dr, c + dc
                    if (
                        rOffset in range(ROWS) and
                        cOffset in range(COLS) and
                        grid[rOffset][cOffset] == 1
                    ):
                        grid[rOffset][cOffset] = 2
                        rottingQ.append((rOffset,cOffset))
                        fresh -= 1
            # add time each "round" we completely deplete Q
            minsElapsed += 1
        if fresh == 0:
            return minsElapsed
        else:
            return -1


# remember deque gets pulled from collections not native to PY
