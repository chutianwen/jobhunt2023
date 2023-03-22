import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        end = len(tokens)
        cur_idx = 0
        ops = '+-*/'

        while cur_idx < end:
            letter = tokens[cur_idx]
            if letter not in ops:
                stack.append(int(letter))
            else:
                last = stack.pop()
                second_last = stack.pop()
                if letter == '+':
                    stack.append(last + second_last)
                elif letter == '-':
                    stack.append(second_last - last)
                elif letter == '*':
                    stack.append(second_last * last)
                else:
                    division = second_last / last
                    stack.append(math.floor(division) if division  >= 0 else math.ceil(division))
            cur_idx += 1

        return stack.pop()