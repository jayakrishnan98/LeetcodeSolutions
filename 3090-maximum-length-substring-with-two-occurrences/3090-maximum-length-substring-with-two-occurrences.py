class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = Counter()
        result = 0
        start = -1

        for end, char in enumerate(s):
            freq[char] += 1
            while freq[char] > 2:
                start += 1
                freq[s[start]] -= 1
            result = max(result, end-start)

        return result