class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = None
        count = 0
        for num in nums:
            if count == 0:
                value = num
            if num == value:
                count += 1
            else:
                count -= 1
        
        return value