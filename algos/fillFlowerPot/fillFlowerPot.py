# given a 2d array like the following:
# [
#     [1, 0, 0, 1, 1],
#     [1, 1, 0, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 0, 1, 1, 0],
#     [1, 1, 0, 0, 0]
# ]
# where 1 represents a piece of gravel and 0 represents an empty space.
# I want it to use a 2d array to represent a flower pot.
# its important to make sure that whenever you water your plant any water that doesn't get absorbed by the roots drains to the bottom of the pot.

# I need the function to return whether there is a route of 0's
# from the top row, which reaches the bottom row, contiguous,
# only moving up, right, left or down (not diagonal)

from collections import deque
from typing import List


class Solution:
  def fillFlowerPot(self, pot: List[List[int]]) -> bool:
    m = len(pot)
    n = len(pot[0])
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    q = deque()

    # fill initial queue with any 0's on top row
    for j in range(n):
      if (pot[0][j] == 0):
        q.append([0,j])
        pot[0][j] = 2
    
    while q:
      layer = q.popleft()
      i = layer[0]
      j = layer[1]

      for direction in directions:
        i_offset, j_offset = direction
        r = i + i_offset
        c = j + j_offset

        if (r >= 0 and r < m and c >= 0 and c < n and pot[r][c] == 0):
          q.append([r,c])
          pot[r][c] = 2

    last_row = pot[-1]
    if 0 in last_row:
      return True
    else:
      return False

pot = [
    [1, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0]
]

my_solution = Solution()

result = my_solution.fillFlowerPot(pot)
print(result)