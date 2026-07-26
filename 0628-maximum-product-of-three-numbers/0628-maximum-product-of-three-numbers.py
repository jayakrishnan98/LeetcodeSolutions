import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return math.prod(nums)

        first = second = third = float('-inf')
        last = scnd_last = float('inf')

        for num in nums:
            if num > first:
                third, second, first = second, first, num
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num
            
            if num < last:
                scnd_last, last = last, num
            elif num < scnd_last:
                scnd_last = num

        return max((first * second * third),(last * scnd_last * first))


