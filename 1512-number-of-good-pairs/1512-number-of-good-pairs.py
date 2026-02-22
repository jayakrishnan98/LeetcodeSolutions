class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = {}
        sum = 0
        for num in nums:
            if num in a:
                a[num] += 1
                sum += a[num]
            else:
                a[num] = 0
        return sum