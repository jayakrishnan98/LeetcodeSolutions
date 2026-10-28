class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        temp = []

        k = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[k] = nums[i]
                k += 1 
            else:
                temp.append(nums[i])

        for num in temp:
            nums[k] = num
            k += 1

        return nums