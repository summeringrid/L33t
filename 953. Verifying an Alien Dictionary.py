class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # construct an order sys for the alien dict
        dict_order = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):  # w1 is not a prefix of w2
                    return False

                if w1[j] != w2[j]:
                    if dict_order[w1[j]] > dict_order[w2[j]]:
                        return False
                    break
        return True

        # Time = O(n)
        # Space = O(n)