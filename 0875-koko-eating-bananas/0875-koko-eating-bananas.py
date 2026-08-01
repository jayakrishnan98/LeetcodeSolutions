class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            required_hours = 0

            for pile in piles:
                required_hours += pile // mid
                if pile % mid != 0:
                    required_hours += 1

            if required_hours > h:
                # Too slow
                left = mid + 1
            else:
                # Works, but search for a smaller valid speed
                right = mid

        return left