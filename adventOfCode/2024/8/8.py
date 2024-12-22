import math
import os
import sys
from typing import Dict, List, Set, Tuple

script_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(script_dir)
root_dir = os.path.dirname(parent_dir)

sys.path.append(root_dir)

from util import parse_input

"""
[
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

If I'm interpreting the question correctly, we actually care about REAL DISTANCE
between 2 nodes using pythagorean theorem, rather than assumed difference via subtraction.
Shrug

for each unique character, build set of all coordinates of character
0 set { (1,8) (2,5) (3,7) (4,4)}
A set { (5,6) (8,8) (9,9)}

create master Set of antinode coords

for each unique character (frequency group),
  for each pair in character Set (each antenna A1),
    for every other pair in character Set (every other antenna A2),
      calculate antinode coords:
      potential 2 antinode points where the distance to A2 is twice the distance to A2
      check if each potential antinode is in bounds
      add to master Set if valid

return length of master set
"""
def collect_antennas(board: List[List[str]]) -> Dict[str, Set[Tuple[int, int]]]:
  # return like { "0": Set{} }
  antennas = {}
  for i, row in enumerate(board):
    for j, char in enumerate(row):
      if char != '.':
        if char not in antennas:
          antennas[char] = set()
        antennas[char].add((i,j))
  return antennas

def get_coord_difference(p1: Tuple[int,int], p2: Tuple[int,int]) -> Tuple[int,int]:
  return (p2[0]-p1[0],p1[1]-p1[1])

def find_antinode_points(a1: Tuple[int,int], a2: Tuple[int,int]) -> List[Tuple[float,float]]:
  """
  find 2 antinode points for a pair of antennas where:
  - points lie to eiether side in a line between 2 antennas
  - one point is twice as far from the antenna as the other
  returns list of (x,y) coords for antinode points
  """
  diff = get_coord_difference(a1,a2)
  # first antinode - move backward frm a1
  p1 = (a1[0]-diff[0],a1[1]-diff[1])

  # second antnode - move forward form a2
  p2 = (a2[0]+diff[0],a2[1]+diff[1])
  
  return [p1,p2]

def is_in_bounds(point: Tuple[float, float], board: List[List[str]]) -> bool:
  x,y = point
  return 0 <= x < len(board) and 0 <= y < len(board[0])

def interpret(board: List[List[str]]) -> Set[Tuple[int,int]]:
  antinodes = set()
  antennas = collect_antennas(board)

  # for each frequency group
  for antenna_set in antennas.values():
    # for each pair of antennas in the group
    for a1 in antenna_set:
      for a2 in antenna_set:
        if a1 != a2:
          # find all potentiall antinode points
          points = find_antinode_points(a1,a2)
          # add valid points to set
          for point in points:
            if is_in_bounds(point, board):
              #round coordinates for the final set
              antinodes.add(point)
  return antinodes


if __name__  == '__main__':
  board = parse_input('8-input.txt')
  board = [list(line) for line in board]
  print(board)
  res = interpret(board)
  print(len(res))