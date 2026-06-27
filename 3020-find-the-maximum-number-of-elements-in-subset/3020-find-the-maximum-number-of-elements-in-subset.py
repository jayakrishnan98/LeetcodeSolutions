from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Special case for 1
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 else freq[1] - 1)

        # Try every possible starting value
        for x in freq:
            if x == 1:
                continue

            curr = x
            length = 0

            while freq[curr] >= 2:
                length += 2
                curr *= curr

            # Current value can be used once if it exists
            if freq[curr] == 1:
                length += 1
            else:
                # We counted two copies of the previous value,
                # but one of them must become the center.
                length -= 1

            ans = max(ans, length)

        return ans