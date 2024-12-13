"""
from starting point move in direction:
 if > move right etc.
if next space is open:
move forward
log space in visited set
if next space is obstacle:
cycle to next clockwise caret
if next space is off board, move off board and end
return visited length
"""

import os
import sys

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
root_dir = os.path.dirname(parent_dir)

sys.path.append(root_dir)

from util import parse_input

def interpret(board):
  positions = ['^','>','v','<']
  ROWS = len(board)
  COLS = len(board[0])
  directions = [(-1,0),(0,1),(1,0),(0,-1)]

  starting_pos_i = 0
  starting_pos_j = 0
  for i in range(ROWS):
    for j in range(COLS):
      if board[i][j] in positions:
        starting_pos_i = i
        starting_pos_j = j
  starting_direction = positions.index(board[starting_pos_i][starting_pos_j])
  
  visited = set([(starting_pos_i, starting_pos_j)])
  curr_i, curr_j = starting_pos_i, starting_pos_j
  curr_dir = starting_direction

  while True:
    # calculate next position
    next_i = curr_i + directions[curr_dir][0]
    next_j = curr_j + directions[curr_dir][1]
    #check if off board
    if (next_i < 0 or next_i >= ROWS or next_j < 0 or next_j >=  COLS):
      break
    # check if obstacle
    if board[next_i][next_j] == '#':
      curr_dir = (curr_dir + 1) % 4
    else:
      curr_i, curr_j = next_i, next_j
      visited.add((curr_i, curr_j))
  return len(visited)

if __name__  == '__main__':
  board = parse_input('6-input.txt')
  board = [list(line) for line in board]
  res = interpret(board)
  print(res)