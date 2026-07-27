class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current, left, right):
            if left == n and right == n:
                result.append(current)
                return
            
            if left < n:
                backtrack(current + '(', left + 1, right)
            if right < left:
                backtrack(current + ')', left, right + 1)
            

        backtrack("", 0, 0)
        return result