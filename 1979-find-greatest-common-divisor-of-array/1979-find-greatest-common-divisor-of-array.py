class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[len(nums)-1]
        print(nums)
        print(a)
        print(b)
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return i