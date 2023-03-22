class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        end = len(s)
        cur_idx = 0
        amount = 0

        while cur_idx < end:
            if cur_idx < end - 1 and symbol_value_map[s[cur_idx + 1]] > symbol_value_map[s[cur_idx]]:
                amount += symbol_value_map[s[cur_idx + 1]] - symbol_value_map[s[cur_idx]]
                cur_idx += 2
            else:
                amount += symbol_value_map[s[cur_idx]]
                cur_idx += 1

        return amount
