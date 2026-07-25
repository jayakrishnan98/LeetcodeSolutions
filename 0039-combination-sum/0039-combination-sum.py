class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start, current, remaining):

            if remaining == 0:
                result.append(current.copy())
                return
                
            elif remaining < 0:
                return 

            for index in range(start, len(candidates)):
                if candidates[index] > remaining:
                    break
                item = candidates[index]
                current.append(item)
                backtrack(index, current, remaining-item)
                current.pop()
                
        backtrack(0, [], target)
        return result