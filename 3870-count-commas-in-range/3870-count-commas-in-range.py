class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        for i in range(1000, n+1):
            count += 1
        
        return count