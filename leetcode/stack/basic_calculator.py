class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += "$"
        len_s = len(s)

        def driver(i):
            stack = []
            sign = "+"
            number = 0
            while i < len_s:
                letter = s[i]

                if letter == " ":
                    i += 1
                    continue
                elif letter.isdigit():
                    number = number * 10 + int(letter)
                    i += 1
                elif letter == "(":
                    number, i = driver(i + 1)
                else:
                    print(number, sign)

                    if sign == "+":
                        stack.append(number)
                        number = 0
                    if sign == "-":
                        stack.append(-number)
                        number = 0
                    if sign == "*":
                        stack[-1] *= number
                    if sign == "/":
                        stack[-1] = stack[-1] // number if stack[-1] >= 0 else -(-stack[-1] // number)

                    i += 1
                    if letter == ")":
                        return sum(stack), i
                    sign = letter

            return sum(stack)

        return driver(0)

res = Solution().calculate('5-66')
print(res)