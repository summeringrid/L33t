class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                # 0,1,5,9 -> ↑ 1,2,6,0      ++  -> +1 %10
                #         -> ↓ 9,1,4,8      --  ->(-1 + 10) %10

                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        q = deque()
        q.append(['0000', 0])  # [lock, turns]
        visited = set(deadends)
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    q.append([child, turns + 1])
                    visited.add(child)
        return -1
        # not sure

        # Time = O(4*10000)  -> O(1)    worst case
        # Space = O(10^4)