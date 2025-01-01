def parse_text(filename):
  with open(filename, "r") as file:
    lines = []
    for line in file:
      lines.append(list(line.strip()))
  return lines

def bfs_grid(grid: list(list(str))) -> int:
  return 9

# [
#   ['8', '9', '0', '1', '0', '1', '2', '3'],
#   ['7', '8', '1', '2', '1', '8', '7', '4'],
#   ['8', '7', '4', '3', '0', '9', '6', '5'],
#   ['9', '6', '5', '4', '9', '8', '7', '4'],
#   ['4', '5', '6', '7', '8', '9', '0', '3'],
#   ['3', '2', '0', '1', '9', '0', '1', '2'],
#   ['0', '1', '3', '2', '9', '8', '0', '1'],
#   ['1', '0', '4', '5', '6', '7', '3', '2']]

if __name__ == '__main__':
  parsed_text = parse_text('10-input.txt')
  print(parsed_text)
  num_paths = bfs_grid(parsed_text)
  print(num_paths)