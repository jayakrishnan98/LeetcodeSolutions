class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:

            mid = left + (right - left)//2
            print(mid)
            # if left half is sorted
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[mid]