from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def find_actual_days(max_weight: int) -> int:
            actual_days = 1
            current_sum = 0

            for weight in weights:
                # Package cannot fit on the current day
                if current_sum + weight > max_weight:
                    actual_days += 1
                    current_sum = 0

                current_sum += weight

            return actual_days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            actual_days = find_actual_days(mid)

            if actual_days > days:
                # Capacity is too small
                left = mid + 1
            else:
                # Capacity works; try a smaller capacity
                right = mid

        return left