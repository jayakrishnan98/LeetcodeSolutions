class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, char_set = 0, set()
        max_len = 0
        for right in range(len(s)):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            max_len = max(max_len, right-left + 1)
            char_set.add(s[right])

        return max_len