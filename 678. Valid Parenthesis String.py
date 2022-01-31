class Solution:
    def checkValidString(self, s: str) -> bool:
        # brutal force: decision tree --> 3^n

        minLeft, maxLeft = 0, 0

        for c in s:
            if c == '(':
                minLeft, maxLeft = minLeft + 1, maxLeft + 1
            elif c == ')':
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            else:  # c == '*':
                minLeft, maxLeft = minLeft - 1, maxLeft + 1
            if maxLeft < 0:
                return False
            if minLeft < 0:  # whenever it becomes -1
                minLeft = 0

        return minLeft == 0

    # Time = O(n), Space = O(1)