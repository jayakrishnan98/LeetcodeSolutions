class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cur_max = 0

        for num in nums:
            if num == 1:
                cur_max += 1
                result = max(cur_max, result)
            else:
                cur_max = 0
        
        return result