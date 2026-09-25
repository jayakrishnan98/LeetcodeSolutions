class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        def backtrack(current):
            if len(nums) == len(current):
                result.append(current.copy())
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        
        result = []
        backtrack([])
        return result