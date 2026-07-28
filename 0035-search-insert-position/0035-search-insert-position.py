class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leng = len(nums)
        
        left, right = 0, leng
        mid = 0
        while left<right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left