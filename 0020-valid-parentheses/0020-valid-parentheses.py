class Solution:
    def isValid(self, s: str) -> bool:
        
        char_map = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for char in s:
            if char not in char_map:
                stack.append(char)
            else:
                last = stack.pop() if len(stack) else "#"
                if last != char_map[char]:
                    return False
            
        return True if not len(stack) else False