class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        for word in a[::-1]:
            if len(word) > 0 and word != " ":
                return len(word)
        return 0