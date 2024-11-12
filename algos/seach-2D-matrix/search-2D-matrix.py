class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        in this example I don't understand why you wouldn't
        just want to flatten the 2d array and run a binary
        search but OK here we go

        I think what we do here is first run a binary search vertically
        on the first element of each row, and eventually find a 
        row where target >= row[0] and target < row+1[0]

        Then run a binary search on that row
        """

        ### FLATTEN AND B SEARCH

        flattened_list = [] ## [1,2,3,4]

        # N pass
        for item in matrix:
            for dig in item:
                flattened_list.append(dig)
        print(flattened_list)

        # binary search
        L, R = 0, len(flattened_list)
        while L <= R:
            M = L + ((R-L) // 2)
            if (flattened_list[M] > target):
                R = M - 1
            elif (flattened_list[M] < target):
                L = M + 1
            else:
                return True
        return False

    def searchMatrixDoubleBinarySearch(self, matrix: List[List[int]], target: int) -> bool:
        """
        approach: binary search the rows themselves.
        We know the last value of each row is less than the first value of the next row.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # binary search the rows themselves
        top, bottom = 0, ROWS-1
        while top <= bottom:
            middlerow = (top + bottom) // 2
            if target > matrix[middlerow][-1]:
                top = middlerow+1
            elif target < matrix[middlerow][0]:
                bottom = middlerow-1
            else:
                break
        if not (top <= bottom):
            return False

        # then when we find the right row, binary search the row:
        row = (top + bottom) // 2
        L,R = 0, COLS-1
        while L <= R:
            m = (L+R) // 2
            if target > matrix[row][m]:
                L = m+1
            elif target < matrix[row][m]:
                R = m-1
            else:
                return True
        return False
 




