from typing import List, Tuple
import math

def get_num_digits(num: int) -> int:
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1

def get_left_right_number(num: int) -> Tuple[int,int]:
   num_string = str(num)
   length = len(num_string)
   mid = length // 2 # floor
   left = int(num_string[:mid])
   right = int(num_string[mid:])
   return left, right

def process_input(input):
  """
  I think the trick here will be with large inputs, we want to do this in-place.
  Let's first try by creating extra memory and see if we run into timeout error.
  """
  newList = input
  tempNewList = []
  for _ in range(0,25):
    for number in newList:
      if number == 0:
        tempNewList.append(1)
        continue
      num_digits_of_number = get_num_digits(number)
      if num_digits_of_number % 2 == 0:
        left, right = get_left_right_number(number)
        tempNewList.append(left)
        tempNewList.append(right)
        continue
      tempNewList.append(number * 2024)
    newList = tempNewList
    tempNewList = []
  return newList

  

input = [77,515,6779622,6,91370,959685,0,9861]

def main(input: List[int]) -> None:
  total = process_input(input)
  print(len(total))

main(input)