from collections import deque

#  [emp, WAL, GAT, emp],
#  [emp, emp, emp, WAL],
#  [emp, WAL, emp, WAL],
#  [GAT, WAL, emp, emp]

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead
    """
    ROWS, COLS = len(rooms), len(rooms[0])
    visit = set()
    q = deque()

    def addRoom(r, c):
      if (r < 0 or r == ROWS or c < 0 or c == COLS or
      (r, c) in visit or rooms[r][c] == -1):
        return
      visit.add((r,c))
      q.append([r,c])


    for r in range(ROWS):
      for c in range(COLS):
        if rooms[r][c] == 0:
          q.append([r,c])
          visit.add([r,c])

    dist = 0
    while q:
      for i in range(len(q)):
        r, c = q.popleft() # get coordinates of 'layer'

        # change this layer to be the current distance
        rooms[r][c] = dist

        addRoom(r+1, c) # add every neighbor of this room
        addRoom(r-1, c)
        addRoom(r, c+1)
        addRoom(r, c-1)

      dist += 1 #increment distance each time we complete 'layer'
