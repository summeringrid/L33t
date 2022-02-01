class Solution:
    def calculate(self, s: str) -> int:
        # isdigit(), isspace(), ord('char') - ord('0')
        # stack.append(val), stack.pop()
        if not str:
            return 0

        stack, num, sign = [], 0, +
        for i in str:
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(str) - 1:  # HINT: NOT THE LAST DIGIT
                if s[i] == "+":
                    stack.append(num)
                elif s[i] == "-":
                    stack.append(-num)
                elif s[i] == "*":
                    stack.append(stack.pop() * num)
                else:  # s[i] == "/"

                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        # deal with it
                        stack.append(tmp // num + 1)

                    else:  # temp//num >= 0 and tmp&num == 0
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)

        # Time = O(n), Space = O(1)