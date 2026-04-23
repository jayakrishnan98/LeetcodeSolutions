class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []

        for word in s:
            if stack and stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        
        return "".join(stack)