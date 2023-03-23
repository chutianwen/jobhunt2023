class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        remain = 0
        total = 0
        candidate = 0

        for idx, gas in enumerate(gas):
            total += gas - cost[idx]
            remain += gas - cost[idx]
            if remain < 0:
                remain = 0
                candidate = idx + 1

        if total < 0:
            return -1
        return candidate
