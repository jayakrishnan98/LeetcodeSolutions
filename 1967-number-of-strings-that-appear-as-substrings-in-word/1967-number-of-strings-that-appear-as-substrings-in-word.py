class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for item in patterns:
            if item in word:
                count += 1
        
        return count