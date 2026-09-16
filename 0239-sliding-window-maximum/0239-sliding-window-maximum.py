class Solution:
# [1,3,-1,-3,5,3,6,7]
# [0,1,2,3,4,5,6,7,8]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        for right in range(len(nums)):
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            q.append(right)

            if q[0] <= right - k:
                q.popleft()

            if right >= k-1:
                result.append(nums[q[0]])
                
        return result