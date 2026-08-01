class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lowerBound(trgt: int)-> int:
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left)//2
                    
                if nums[mid] < trgt:
                    left = mid + 1
                else:
                    right = mid

            return left
        
        first = lowerBound(target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        first_greater = lowerBound(target+1)

        last = first_greater-1

        return [first, last]
