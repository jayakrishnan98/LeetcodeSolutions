class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        left, right = 0, len(nums) - 1
        # Reverse the array
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        #again reverse from 0-kth element
        left, right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        #again reverse from kth - n element
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        