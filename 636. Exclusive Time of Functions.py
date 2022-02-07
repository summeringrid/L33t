class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []

        for log in logs:
            f_id, event, time = log.split(':')
            f_id, time = int(f_id), int(time)
            if event == 'start':
                stack.append([f_id, time])
            else:
                popped = stack.pop()  # [f_id, start time]
                res[popped[0]] += time - popped[1] + 1
                if stack:
                    res[stack[-1][0]] -= time - popped[1] + 1  # HINT: penalty based, minus the occupied time
        return res

        # Time = O(n), n = len(logs)
        # Space = O(n)      - > n/2