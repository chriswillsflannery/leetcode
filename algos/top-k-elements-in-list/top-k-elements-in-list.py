from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}
        for num in nums:
            occurrences[num] = occurrences.get(num, 0) + 1

        # turn into list of tuples?
        # [[1,1], [2,2], [3,3]]
        # sort descending by 2nd val
        # [[3,3], [2,2], [1,1]]
        # slice to return first k tuples
        # only return keys
        items = list(occurrences.items())
        items.sort(key=lambda x: x[1], reverse=True)

        top_k = items[:k]

        return [item[0] for item in top_k]
    
mysol = Solution()
mysol.topKFrequent([1,2,2,3,3,3], 2)

# alternate solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # like [[], [], [] ... ]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # fill occurrences dict
            # { 1: 1, 2: 2 }
        for key, val in count.items():
            freq[val].append(key)
            # [[], [1], [2]]

        res = []
        # syntax: start, stop, step
        for i in range(len(freq) - 1, 0, -1):
            for key in freq[i]:
                res.append(key) # append [2] to [] resulting in [[2]]
                if len(res) == k:
                    return res