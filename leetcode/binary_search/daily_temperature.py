from bisect import bisect_right


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        This is similar to longest increasing subsequence question.
        :param temperatures:
        :return:
        '''
        buffer = []
        answer = [-1 for _ in range(len(temperatures))]
        cur_idx = len(temperatures) - 1

        while cur_idx >= 0:
            cur_temp = temperatures[cur_idx]
            cur_buffer_entry = (cur_temp, cur_idx)
            # print(cur_buffer_entry)
            # print(buffer)
            if not buffer:
                answer[cur_idx] = 0
                buffer.append(cur_buffer_entry)
            else:
                # check current temp position in buffer
                buffer_idx = bisect_right(buffer, (cur_temp, 10 ** 5))

                # nothing in buffer is warmer than current
                if buffer_idx == len(buffer):
                    answer[cur_idx] = 0
                else:
                    next_warmer_temp, next_warmer_idx = buffer[buffer_idx]
                    answer[cur_idx] = next_warmer_idx - cur_idx

                # update buffer
                buffer = [cur_buffer_entry] + buffer[buffer_idx:]
            # print(f'cur_temp:{cur_temp}, answer:{answer[cur_idx]}')
            cur_idx -= 1

        return answer


class StackSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, temp = [], temperatures
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                j = stack.pop()
                temp[j] = i - j
            stack.append(i)
        for _ in range(len(stack)):
            temp[stack.pop()] = 0
        return temp