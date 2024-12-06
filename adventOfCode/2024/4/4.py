def parse_text(filename):
  with open(filename, "r") as file:
    lines = []
    for line in file:
      lines.append(line.strip())
  return lines

def find_occurrences(grid, word):
  pass
  # 8 dirs: forwards backwards horiz, vertical and 4 ways diagonal
  ROWS = len(grid)
  COLS = len(grid[0])
  count = 0

  dirs = [
    (0,1), # to right
    (1,1), # down-right
    (1,0), # down
    (1,-1), # down-left
    (0,-1), # left
    (-1,-1), # up-left
    (-1,0), # up
    (-1,1) # up-right
  ]

  # check word exists starting at row,cal in dir dx,dy:
  def check_word(row,col,dx,dy):
    if (
      0 <= row + (len(word)-1)*dx < ROWS and
      0 <= col + (len(word)-1)*dy < COLS
    ):
      return all(
        grid[row + i*dx][col + i*dy] == word[i]
        for i in range(len(word))
      )
    return False

  # check each starting position
  for i in range(ROWS):
    for j in range(COLS):
      if grid[i][j] == word[0]:
        for dx, dy in dirs:
          if check_word(i,j,dx,dy):
            count += 1
  return count


if __name__ == '__main__':
  parsed_text = parse_text('4-input.txt')
  # convert strings to list of chars
  grid = [list(row) for row in parsed_text]
  res = find_occurrences(grid, "XMAS")
  print(res)