class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def _get_final_string(my_string:str) -> str:
            my_string = list(my_string)
            my_stack = []
            for char in my_string:
                if char != '#':
                    my_stack.append(char)
                else:
                    if my_stack:
                        my_stack.pop()
            return "".join(my_stack)


        a = _get_final_string(s)
        b = _get_final_string(t)

        print(a, b)
        return a == b