class Solution:
    def myAtoi(self, s: str) -> int:
        is_positive = None
        numbers = '0123456789'
        signs = '-+'

        accumulator = ''
        cur_idx = 0
        end = len(s)

        upper_bound = 2 ** 31 - 1
        lower_bound = -2 ** 31

        while cur_idx < end:
            letter = s[cur_idx]
            if letter in signs and is_positive is None and not accumulator:
                is_positive = True if letter == '+' else False
            elif letter in numbers:
                accumulator += letter
            elif letter == ' ' and not accumulator and is_positive is None:
                pass
            else:
                break
            cur_idx += 1

        if accumulator:
            number = int(accumulator)
            number = number if is_positive or is_positive is None else -number

            if number > upper_bound:
                return upper_bound
            elif number < lower_bound:
                return lower_bound
            else:
                return number
        else:
            return 0


