class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(current, remaining, start):
            if remaining == 0:
                result.append(current.copy())
                return 
            
            for index in range(start, len(candidates)):
                item = candidates[index]
                if index > start and item == candidates[index - 1]:
                    continue
                if remaining < item:
                    break
                current.append(item)
                backtrack(current, remaining-item, index + 1)
                current.pop()                        
        backtrack([], target, 0)
        return result