class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0
        for item in nums:
            if first < item:
                second, first = first, item
            elif second < item:
                second = item
            
        return (first - 1 ) * (second - 1)