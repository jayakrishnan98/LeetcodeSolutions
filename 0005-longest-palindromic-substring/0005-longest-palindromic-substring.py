class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Transform the string
        t = "^#" + "#".join(s) + "#$"

        n = len(t)
        P = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):

            # Mirror position of i
            mirror = 2 * center - i

            # If i is inside the current palindrome,
            # reuse previously calculated information
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Try to expand further
            while t[i + (P[i] + 1)] == t[i - (P[i] + 1)]:
                P[i] += 1

            # If palindrome around i extends beyond right,
            # update center and right
            if i + P[i] > right:
                center = i
                right = i + P[i]

        # Find the largest palindrome
        max_len = max(P)
        center_index = P.index(max_len)

        # Convert back to original string
        start = (center_index - max_len) // 2

        return s[start:start + max_len]