class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        i = 0
        while (length + i) <= len(haystack):
            if needle == haystack[i:(len(needle)+i)]:
                return i
            i += 1
        return -1