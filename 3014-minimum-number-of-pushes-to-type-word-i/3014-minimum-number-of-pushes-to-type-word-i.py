import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            value = i//8 + 1
            count += value
        
        return count

