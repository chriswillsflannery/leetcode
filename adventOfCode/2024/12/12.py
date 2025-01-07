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

  area_for_char = {}
  perim_for_char = {}

  def dfs(row: int, col: int, char: str):
    visited.add((row,char))
    ## computing area
    if char in area_for_char:
      area_for_char[char] += 1
    else:
      area_for_char = 1

    for xoffset, yoffset in directions:
      ## computing perimeter
      newx = row + xoffset
      newy = col + yoffset
      if newx < 0 or newx >= ROWS or newy < 0 or newy >= COLS or board[newx][newy] != char:
        if char not in perim_for_char:
          perim_for_char[char] = 1
        else:
          perim_for_char[char] += 1

      if 0 <= newx < ROWS and 0 <= newy < COLS and board[newx][newy] and (newx, newy) not in visited:
        dfs(newx, newy, char)

  for row in ROWS:
    for col in COLS:
      if (row,col) in visited:
        continue
      char = board[row][col]
      dfs(row, col, char)
  
  sum = 0
  for areakey in area_for_char.keys():
    area = area_for_char[areakey]
    perimeter = perim_for_char[areakey]
    total = area * perimeter
    sum += total
  return sum

if __name__  == '__main__':
  board = parse_input('12-input.txt')
  board = [list(line) for line in board]
  areas = parse_board(board)
  print(board)