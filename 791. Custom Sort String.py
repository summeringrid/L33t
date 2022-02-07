class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # brutal force

        counter_s = collections.Counter(s)  # HINT: Counter
        ans = []
        for c in order:
            ans.append(c * counter_s[c])
            counter_s[c] = 0  # HINT: avoid repeatly append in next for loop

        for c in counter_s:  # HINT: remaining c in counter_s not s!!
            ans.append(c * counter_s[c])

        return ''.join(ans)

    # Time = O(N), Space = O(N)
    # built-in collections.Counter() is also O(N)