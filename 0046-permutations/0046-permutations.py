class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(current):
            # A complete permutation is formed
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                # Do not use the same number twice
                if num not in current:
                    # Choose
                    current.append(num)
                    # Explore
                    backtrack(current)
                    # Undo the choice
                    current.pop()

        result = []
        backtrack([])
        return result