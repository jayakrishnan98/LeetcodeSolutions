class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, current):
            current_sum = sum(current)
            if current_sum == target:
                result.append(current.copy())
                return
                
            elif current_sum > target:
                return 

            for index in range(start, len(candidates)):
                item = candidates[index]
                current.append(item)
                backtrack(index, current)
                current.pop()
                
        backtrack(0,[])
        return result