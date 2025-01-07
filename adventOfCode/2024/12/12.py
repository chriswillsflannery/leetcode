import os
import sys
from typing import Dict, List

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
root_dir = os.path.dirname(parent_dir)

sys.path.append(root_dir)

from util import parse_input

def parse_board(board: List[List[str]]) -> int:
  # I don't think there is any way to do BFS on this dataset since there is a possibility of multiple
  # areas of the same character
  # I will have to do foreach character in each line and DFS as many adjacent as possible
  # for area of island we just count how many individual squares have same character
  # for perimeter of island, we check all cells of island, and if it has any edges bordering a different
  # character or invalid spaces (off the board), we count those edges and add them to perimeter
  # remember to strike "visited" cells in a visited set.
  
  ROWS = len(board)
  COLS = len(board[0])

  visited = set()
  directions = [(0,1),(1,0),(0,-1),(-1,0)]

  def get_region_stats(row: int, col: int, char: str):
    region_visited = set()
    area = 0
    perimeter = 0
    stack = [(row,col)] # this could also be deque

    while stack:
      curr_row, curr_col = stack.pop()
      if (curr_row, curr_col) in region_visited:
        continue
        
      region_visited.add((curr_row, curr_col))
      visited.add((curr_row, curr_col))
      area += 1

      for xoffset, yoffset in directions:
        newx = curr_row + xoffset
        newy = curr_col + yoffset

        # check perimter
        if newx < 0 or newx >= ROWS or newy < 0 or newy >= COLS or board[newx][newy] != char:
          perimeter += 1
        elif (newx, newy) not in region_visited:
          stack.append((newx, newy))

    return area * perimeter
  
  total_price = 0
  for row in range(ROWS):
    for col in range(COLS):
      if (row, col) not in visited:
        char = board[row][col]
        region_price = get_region_stats(row,col,char)
        total_price += region_price

  return total_price

if __name__  == '__main__':
  board = parse_input('12-input.txt')
  board = [list(line) for line in board]
  totalprice = parse_board(board)
  print(totalprice)