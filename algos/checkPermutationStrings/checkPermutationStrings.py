# given 2 strings, write a method to check if one is a permutation of the other.
# in other words, they are anagrams?
# is the permutation case sensitive; is God a permutation of dog?
# strings must be same length as one another; easy first check.

# class Solution:
#   def arePerms(self, s1, s2):
#     if len(s1) != len(s2):
#       return False
    
#     # sort both strings, then 1 pointer at index 0
#     # if at any time chars are different. return False
#     sorteds1 = sorted(s1)
#     sorteds2 = sorted(s2)

#     for i in range(len(sorteds1)):
#       if sorteds1[i] != sorteds2[i]:
#         return False
#     return True

# sol = Solution()
# print(sol.arePerms('cat', 'tac'))
# print(sol.arePerms('cat', 'tacit'))

# resulting in additional O(2n) space and O(2logN) time ? double check sort runtime in py

# method 2: check if the 2 strings have identical character counts
# build up a count hash of string 1
# for each char in string 2 remove that char or entry from string1 hash
# at the end, hash should be empty. strings are equal. If not empty, strings not equal

class Solution:
  def checkPerm(self, s1, s2):
    if len(s1) != len(s2):
      return False

    s1dict = {}
    for char in s1:
      s1dict[char] = s1dict.get(char, 0) + 1
    
    for char in s2:
      s1dict[char] = s1dict.get(char, 0) - 1

    print(s1dict)

    # if every value in dict is 0, return True
    # else return False

    for val in dict.values():
      if val != 0:
        return False

    return True

sol = Solution()
print(sol.checkPerm('cat', 'tac'))