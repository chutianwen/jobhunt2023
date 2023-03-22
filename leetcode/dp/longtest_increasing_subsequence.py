from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        increasing_sub_seq = []
        for num in nums:
            insert_idx = bisect_left(increasing_sub_seq, num)
            if insert_idx == len(increasing_sub_seq):
                increasing_sub_seq.append(num)
            else:
                increasing_sub_seq[insert_idx] = num
            # print(f'num: {num}, seq:{increasing_sub_seq}')
        return len(increasing_sub_seq)

        #     res = []
        # for num in nums:
        #     idx = bisect_left(res, num)
        #     if len(res) == idx:
        #         res.append(num)
        #     else:
        #         res[idx] = num

        # return len(res)