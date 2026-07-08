from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # cnt[i] = number of non-zero digits in s[:i]
        cnt = [0] * (n + 1)
        digits = []

        for i, ch in enumerate(s):
            cnt[i + 1] = cnt[i]
            if ch != '0':
                cnt[i + 1] += 1
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix sums of digits
        prefix_sum = [0] * (m + 1)

        # prefix concatenated values
        prefix_val = [0] * (m + 1)

        for i, d in enumerate(digits):
            prefix_sum[i + 1] = prefix_sum[i] + d
            prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            L = cnt[l]
            R = cnt[r + 1] - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            digit_sum = prefix_sum[R + 1] - prefix_sum[L]

            value = (
                prefix_val[R + 1]
                - prefix_val[L] * pow10[length]
            ) % MOD

            ans.append((value * digit_sum) % MOD)

        return ans