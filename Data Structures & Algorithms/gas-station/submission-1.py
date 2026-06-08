class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalCost = sum(cost)
        totalGas = sum(gas)

        if totalGas < totalCost:
            return -1

        tank = 0
        count = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                count = i + 1

        return count

        