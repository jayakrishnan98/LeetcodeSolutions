from typing import List

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        bit = BIT(2 * n + 1)

        prefix = n + 1      # offset to avoid negative indices
        bit.update(prefix, 1)

        ans = 0

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix - 1)
            bit.update(prefix, 1)

        return ans