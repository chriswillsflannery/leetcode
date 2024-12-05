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

if __name__ ==  "__main__":
  parsed_text = parse_text('3-input.txt')
  summer = sum_muls(parsed_text)
  print(summer)