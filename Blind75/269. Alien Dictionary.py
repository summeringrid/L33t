class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # DFS  ======================================================================
        # post order dfs: start with the leaves
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):  # go through every single pair of words
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}  # False = visited, True = visited & it's in the current path
        res = []

        def dfs(c):  # post-order dfs
            if c in visit:
                return visit[c]  # alreay in the current path

            visit[c] = True  # not only be visited, but also in the current path now

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        # Time = O(C), D is number of characters in the given words

        # BFS   bookkeeping thing  ==================================================
