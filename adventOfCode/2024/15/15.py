def parse_input_grid(filename):
  lines = []
  with open(filename, 'r') as file:
    for line in file:
      lines.append([char for char in line.strip()])
  return lines

def parse_input_directions(filename):
  directions = ''
  with open(filename, 'r') as file:
    for line in file:
      directions += line.strip()
  return directions

def can_push(grid, row, col, drow, dcol):
  curr_row, curr_col = row, col
  while grid[curr_row + drow][curr_col + dcol] == 'O':
    curr_row += drow
    curr_col += dcol
  
  # final position is empty
  return grid[curr_row + drow][curr_col + dcol] == '.'

def process_move(grid, row, col, drow, dcol):
  next_row = row + drow
  next_col = col + dcol
  
  # do nothing - wall
  if grid[next_row][next_col] == '#':
      return row, col
      
  # empty space - move robot
  if grid[next_row][next_col] == '.':
      grid[row][col] = '.'
      grid[next_row][next_col] = '@'
      return next_row, next_col
      
  # box - check if we can push
  if grid[next_row][next_col] == 'O':
    if can_push(grid, next_row, next_col, drow, dcol):
      # find empty space to move all lined up items
      curr_row = next_row
      curr_col = next_col
      while grid[curr_row][curr_col] == 'O':
        curr_row += drow
        curr_col += dcol
      
      # move all lined up items to empty space
      while curr_row != next_row or curr_col != next_col:
        grid[curr_row][curr_col] = 'O'
        curr_row -= drow
        curr_col -= dcol
      
      # move robot
      grid[curr_row][curr_col] = '@'
      grid[row][col] = '.'
      return next_row, next_col
        
  return row, col

def move(grid, directions):
  # init robot position
  robot_row = robot_col = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == '@':
        robot_row, robot_col = row, col
    
  dir_map = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
  }
    
  for dir in directions:
    drow, dcol = dir_map[dir]
    robot_row, robot_col = process_move(grid, robot_row, robot_col, drow, dcol)
  
  return grid

def print_grid(grid):
  for row in grid:
    print(''.join(row))
  print()

if __name__ == "__main__":
  grid = parse_input_grid('15-grid.txt')
  directions = parse_input_directions('15-directions.txt')
  
  print("Initial state:")
  print_grid(grid)
  
  for dir in directions:
    print(f"Move {dir}:")
    move(grid, dir)
    print_grid(grid)