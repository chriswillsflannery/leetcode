"""
use greedy approach
[[10,100],[10,1000],[50,500],[1,100]]

100-10 = 90 -> it will cost us 90 more to send person 0 to city B
diff = [90, 990, 450, 99]
because all in diff are positive, this tells us that in all cases,
it would be cheaper to send person to city A than city B.

Now we have a list of 4 opportunity costs. And we can say:
of these 4 people, which 2 (half of 4) are cheapest to send to city B?
That's person 0, and person 3. (90, 99)

So we can say:
person 0 -> city B
person 1 -> City A
person 2 -> city A
person 3 -> city B

remember that we need to return the total minimum cost. so for each 
value in our diff array, we need to preserve the [acost, bcost] which
each value maps to.

"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for cityA, cityB in costs:
            cityDiff = abs(cityA - cityB)
            diffs.append(cityDiff, cityA, cityB)
        diffs.sort()
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        return res