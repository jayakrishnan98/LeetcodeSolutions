class Solution:
    def numberOfSteps(self, num: int) -> int:
        sum = 0
        while num != 0:
            sum += 1
            if(num%2 != 0):
                num -= 1
            else: 
                num = num/2
        
        return sum