class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sub_list = nums[n:]
        outArray = []
        for i in range(n):
                outArray.append(nums[i])
                outArray.append(sub_list[i])
        return outArray