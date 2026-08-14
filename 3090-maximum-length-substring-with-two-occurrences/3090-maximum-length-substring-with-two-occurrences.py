class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = Counter()
        result = 0
        start = -1

        for end in range(len(s)):
            freq[s[end]] += 1
            while freq[s[end]] > 2:
                start += 1
                freq[s[start]] -= 1
            result = max(result, end-start)

        return result