class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        total = 0
        station = 0
        for i in range (len(gas)):
            tank += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                station = i + 1
        
        if total < 0:
            return -1
        return station


        