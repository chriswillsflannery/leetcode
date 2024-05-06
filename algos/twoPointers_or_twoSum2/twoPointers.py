class Solution:
  def twoPointers(self, numbers: list[int], target: int):
    l = 0
    r = n - 1
    n = len(numbers)

    while l < r:
      sum = numbers[l] + numbers[r]
      if sum == target:
        return [l, r]
      elif sum < target:
        l += 1
      else:
        r -= 1