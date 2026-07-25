class Solution:
    def maxProduct(self, n: int) -> int:
        highest = second_highest = 0
        while n > 0:
            rem = n % 10
            if rem > highest:
                second_highest = highest
                highest = rem
            elif rem > second_highest:
                second_highest = rem
            n = n // 10
        
        return highest * second_highest
        
        