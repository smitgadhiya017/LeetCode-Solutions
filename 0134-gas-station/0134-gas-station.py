class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalgas = 0
        totalcost = 0
        currgas = 0 
        start = 0

        for i in range(len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]
            currgas += (gas[i] - cost[i])

            if currgas < 0:
                start = i+1
                currgas = 0

        if totalgas < totalcost:
            return -1
        return start