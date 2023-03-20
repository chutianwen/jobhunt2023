class Solution:
    def hammingWeight(self, n: int) -> int:
        comparator = 1
        cnt = 0
        while comparator <= n:
            if (comparator & n) ==  comparator:
                cnt += 1
            comparator <<= 1
        return cnt