class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start, current):
            # We have partitioned the entire string
            if start == len(s):
                result.append(current.copy())
                return

            # Try every possible substring beginning at start
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                # Only choose the substring if it is a palindrome
                if substring == substring[::-1]:
                    current.append(substring)

                    # Partition the remaining part of the string
                    backtrack(end + 1, current)

                    # Undo the choice
                    current.pop()

        backtrack(0, [])

        return result