class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brutal force --> get all possibilities
        # --> split at each index or not (n+1)ways --> Time = 2^n

        # treat each word in the dict as one layer and do a BFS search
        # use queue to track the start index
        # use a hashset to track the visited start index

        queue = deque([0])
        word_set = set(wordDict)
        visited = set()
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            for end in range(1, len(s) + 1):
                if s[start:end] in word_set:
                    queue.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

        # Time = O(n^3) --> queue: n; end point: n; check the word set: m
        # Space = O(n)
