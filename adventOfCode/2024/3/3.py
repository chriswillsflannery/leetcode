"""
get from the plaintext any pattern matches to mul(x,y)
ignore any other characters or invalid formats

ex: 
mul(427,266)#mul(287,390)mul(398,319)#!$>don't()mul(613,600)from()@!{-fro

we extract:
mul(427,266)
mul(287,390)
mul(398,319)

multiply those:
(427 * 266) + (287,390) + (398,319)

Let me know if you understand, and I will proceed to provide you the plaintext.
"""
def parse_text(filename):
  with open(filename, 'r') as file:
      return file.read()
  
import re

def sum_muls(filecontents):
  pattern = r"mul\((\d+),(\d+)\)"
  matches = re.findall(pattern, filecontents)
   
  suma = 0
  for val1,val2 in matches:
    prod = int(val1) * int(val2)
    suma += prod
  return suma

def sum_muls2(filecontents):
    # match literal strings do() and dont()
    do = r"do\(\)"
    dont = r"don't\(\)"
    # use capture groups to match mul(x,y) and extract x,y as group(1) and group(2)
    mul = r"mul\((\d+),(\d+)\)"

    total = 0
    enabled = True
    for x in re.finditer(f"{do}|{dont}|{mul}", filecontents):
      if re.fullmatch(do, x.group()):
        enabled = True
      elif re.fullmatch(dont, x.group()):
        enabled = False
      elif enabled:
        # don't understand enoughh yet about pattern matching to understand why this works
        # where x.group = "mul(x,y)"
        # why does x.group(1) == x
        total += int(x.group(1)) * int(x.group(2))
    return total


if __name__ ==  "__main__":
  parsed_text = parse_text('3-input.txt')
  summer = sum_muls(parsed_text)
  print(summer)

  summer2 = sum_muls2(parsed_text)
  print(summer2)

  ## part 2
  """
  we should parse out any instances of "do()" or "don't()"
  
  Define a regex pattern to match both mul(x,y), don't(), and do()
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
  """