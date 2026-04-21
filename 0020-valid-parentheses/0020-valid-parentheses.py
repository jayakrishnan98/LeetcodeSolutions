class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                top = stack.pop() if len(stack) else '#'
                if mapping[char] != top:
                    return False
        
        return True if not len(stack) else False