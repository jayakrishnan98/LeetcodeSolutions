class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        
        def _reverse(left, right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        _reverse(0, n-1)
        _reverse(0, k-1)
        _reverse(k, n-1)
        
        