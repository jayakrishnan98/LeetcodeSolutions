class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final = 0
        for i in operations:
            if '--' in i:
                final -= 1
            else:
                final += 1
        return final