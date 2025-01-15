from multiprocessing import Pool
from typing import Optional, Tuple, Dict, List

def parse_input(input_text: str) -> List[Dict]:
  machines = []
  current_machine = {}

  for line in input_text.strip().split('\n'):
    if not line:
      continue # empty line

    if line.startswith('Button A:'):
      current_machine = {}
      x, y = line.split('Button A: ')[1].split(', ')
      current_machine['ax'] = int(x.split('+')[1])
      current_machine['ay'] = int(y.split('+')[1])
    elif line.startswith('Button B:'):
      x, y = line.split('Button B: ')[1].split(', ')
      current_machine['bx'] = int(x.split('+')[1])
      current_machine['by'] = int(y.split('+')[1])
    elif line.startswith('Prize:'):
      x, y  = line.split('Prize: ')[1].split(', ')
      current_machine['prize_x'] = int(x.split('=')[1])
      current_machine['prize_y'] = int(y.split('=')[1])
      machines.append(current_machine)
  return machines

def find_solution(machine: Dict) -> Optional[Tuple[int,int.int]]:
  """
  Processing single machine and return (a_presses,
  b_presses, token) if solvable, else return None
  """
  ax, ay = machine['ax'], machine['ay']
  bx, by = machine['bx'], machine['by']
  target_x, target_y = machine['prize_x'], machine['prize_y']

  # try all combinations A and B up to 100
  for a in range(101):
    for b in range(101):
      # check if combination reaches target coords
      if (a * ax + b * bx == target_x) and (a * ay + b * by == target_y):
        tokens = (a * 3) + b
        return (a,b,tokens)
  return None

def solve_puzzle(input_text: str, num_processes: int = None) -> int:
  machines = parse_input(input_text)
  
  with Pool(processes=num_processes) as pool:
    results = pool.map(find_solution, machines)

  total_tokens = 0
  solvable_count = 0

  for i, result in enumerate(results):
    if result:
      a_presses, b_presses, tokens = result
      total_tokens += tokens
      solvable_count += 1
      print(f"machine {i} solved: {a_presses} A presses and {b_presses} B presses ({tokens} tokens)")
    else:
      print(f"Machine {i} no solution found")
      
  print(f"total solvable machines: {solvable_count}")
  print(f"total tokens needed: {total_tokens}")
  return total_tokens

example_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

res = solve_puzzle(example_input)
print(res)