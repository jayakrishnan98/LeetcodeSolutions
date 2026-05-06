class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        my_arr = path.split('/')

        for part in my_arr:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
            
        return '/' + '/'.join(stack)