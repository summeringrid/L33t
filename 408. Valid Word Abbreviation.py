class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = a = 0
        wLen, aLen = len(word), len(abbr)
        while w < wLen and a < aLen:
            if word[w] == abbr[a]:
                w += 1
                a += 1
            elif abbr[a] == '0':
                return False
            elif abbr[a].isnumeric():
                i = a
                while i < aLen and abbr[i].isnumeric():
                    i += 1
                w += int(abbr[a:i])
                a = i
            else:
                return False
        return w == wLen and a == aLen

    # Time = O(N), Space = O(1)