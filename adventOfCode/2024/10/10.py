from collections import deque
from typing import List


def parse_text(filename):
  with open(filename, "r") as file:
    lines = []
    for line in file:
      lines.append([int(char) for char in line.strip()])
  return lines

def dfs_grid(grid: List[List[int]]) -> int:
  ROWS = len(grid)
  COLS = len(grid[0])
  directions = [(0,1),(1,0),(0,-1),(-1,0)]

  def dfs(r: int, c: int, visited: set, reachable_nines: set) -> None:
    if grid[r][c] == 9:
      reachable_nines.add((r,c))
      return
    
    current_height = grid[r][c]

    for dx, dy in directions:
      r_offset,c_offset = r+dx, c+dy
      if (0 <= r_offset < ROWS and
          0 <= c_offset < COLS and
          grid[r_offset][c_offset] == current_height + 1 and
          (r_offset, c_offset) not in visited):
        visited.add((r_offset,c_offset))
        dfs(r_offset,c_offset,visited,reachable_nines)
        #backtrack - remove from visited
        visited.remove((r_offset, c_offset))
  total_score = 0

  #find all trailheads
  for i in range(ROWS):
    for j in range(COLS):
      if grid[i][j] == 0:
        # for each trailhead find reachable nines
        reachable_nines = set()
        dfs(i,j,{(i,j)},reachable_nines)
        score = len(reachable_nines)
        total_score += score
  return total_score

if __name__ == '__main__':
  parsed_text = parse_text('10-input.txt')
  print(parsed_text)
  num_paths = dfs_grid(parsed_text)
  print(num_paths)