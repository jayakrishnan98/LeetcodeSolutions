class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length ==1:
            return nums[0]
        def rob_default(my_list):
            back_two_steps, previous_step = 0, 0

            for money in my_list:
                skip_current = previous_step
                rob_current = money + back_two_steps

                current_best = max(skip_current, rob_current)

                back_two_steps, previous_step = previous_step, current_best
            
            return previous_step
        
        return max(rob_default(nums[1:]), rob_default(nums[:-1]))
