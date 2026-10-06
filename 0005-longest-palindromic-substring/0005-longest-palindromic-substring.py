class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # We went one step too far on both sides
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length: "aba"
            left1, right1 = expand(i, i)

            # Even length: "abba"
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]