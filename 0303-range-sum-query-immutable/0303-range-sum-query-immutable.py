class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0] * len(nums)
        sum_so_far = 0
        for idx, num in enumerate(nums):
            sum_so_far += num
            self.prefix[idx] = sum_so_far

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)