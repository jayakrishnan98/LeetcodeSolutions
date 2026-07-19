class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, current):
            result.append(current.copy())

            for index in range(start, len(nums)):

                if index > start and nums[index] == nums[index-1]:
                    continue

                current.append(nums[index])
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])
        return result


