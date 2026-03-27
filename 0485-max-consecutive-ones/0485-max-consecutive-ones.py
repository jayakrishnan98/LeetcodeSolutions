class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max = 0
        act_max = 0
        for num in nums:
            if num == 1:
                cur_max += 1
                if cur_max > act_max:
                    act_max = cur_max
            else:
                cur_max = 0
        return act_max