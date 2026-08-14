class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0] * 26
        result = 0
        start = -1

        for end, char in enumerate(s):
            char_index = ord(char) - ord('a')
            freq[char_index] += 1
            while freq[char_index] > 2:
                start += 1
                removed_char = ord(s[start]) - ord('a')
                freq[removed_char] -= 1
            result = max(result, end-start)

        return result