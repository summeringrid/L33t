class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # linear traverse
        ans = []

        for cur in range(len(heights)):
            # heights = [4,2,3,1]
            #     ans = [0,2,3]
            #       h =  4,3,1
            while ans and heights[ans[-1]] <= heights[cur]:
                ans.pop()
            ans.append(cur)

        return ans
        # Time = O(N), N = len(heights), Space = O(N)
        # ============================================
        # Optimized --> Monotonic Stack

        # heights = [4,2,3,1] ---> reversed: [1,3,2,4]
        #                                     √,√,X,√

        ans = []
        max_height = 0
        for cur in reversed(range(len(heights))):
            if heights[cur] > max_height:
                ans.append(cur)
                max_height = max(max_height, heights[cur])
        ans.reverse()
        return ans
        # Time = O(N), N = len(heights), Space = O(1)



