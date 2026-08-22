class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        sum = 0
        product = 1
        original = n

        while n > 0:
            digit = n % 10
            sum = sum + digit
            product = product * digit
            n = n//10
        
        return original % (sum + product) == 0