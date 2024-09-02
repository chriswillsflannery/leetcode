from collections import defaultdict
from typing import List


class Solution:
  def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    for string in strings:
      # like [0,0,0,0]
      # representing freq of each char of alphabet
      count = [0] * 26
      for char in string:
        count[ord(char) - ord('a')] += 1
        # ord() returns the ascii int value of a char
        # eg. ord('a') returns 97
        # so ord('c') - ord('a') returns 2, the correct position for c in 26 chars
      ans[tuple(count)].append(string)
      # print(ans)
    return ans.values()
    
sol = Solution()
solution = sol.groupAnagrams(['abc', 'cba', 'cars', 'rats'])
print(solution)