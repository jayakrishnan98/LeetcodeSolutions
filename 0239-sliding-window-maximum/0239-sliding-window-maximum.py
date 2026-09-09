class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        result = []
        q = collections.deque()
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # Remove indices that are outside the window
            if q[0] < left:
                q.popleft()

            # Window has reached size k
            if (right - left) + 1 == k:
                result.append(nums[q[0]])
                left += 1

        return result