class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # early return false if sum(gas) < sum(cost)
        totalGas = 0
        for gasi in gas:
            totalGas += gasi
        totalCost = 0
        for costi in cost:
            totalCost += costi
        
        if totalGas < totalCost:
            return -1
        
        """
        optimized use python builtins:
        if sum(gas) < sum(cost):
            return -1
        """

        startPos = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                startPos = i + 1
        return startPos






