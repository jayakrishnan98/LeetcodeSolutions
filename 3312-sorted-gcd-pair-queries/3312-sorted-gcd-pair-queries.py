from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(
        self,
        nums: List[int],
        queries: List[int]
    ) -> List[int]:

        max_value = max(nums)

        # frequency[x] = how many times x appears in nums
        frequency = [0] * (max_value + 1)

        for num in nums:
            frequency[num] += 1

        # gcd_count[g] = number of pairs having GCD exactly g
        gcd_count = [0] * (max_value + 1)

        # Calculate from larger GCD to smaller GCD
        for g in range(max_value, 0, -1):

            divisible_count = 0

            # Count numbers divisible by g
            for multiple in range(g, max_value + 1, g):
                divisible_count += frequency[multiple]

            # Number of pairs where both numbers are divisible by g
            total_pairs = (
                divisible_count * (divisible_count - 1) // 2
            )

            # Remove pairs whose exact GCD is 2g, 3g, 4g, ...
            for multiple in range(2 * g, max_value + 1, g):
                total_pairs -= gcd_count[multiple]

            gcd_count[g] = total_pairs

        # prefix[g] = number of pairs whose GCD <= g
        prefix = [0] * (max_value + 1)

        for g in range(1, max_value + 1):
            prefix[g] = prefix[g - 1] + gcd_count[g]

        answer = []

        for query in queries:
            # First GCD where cumulative pair count > query
            answer.append(bisect_right(prefix, query))

        return answer