from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(text):
            left = 0
            right = len(text) - 1

            while left < right:
                if text[left] != text[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start, current):
            # We have partitioned the entire string
            if start == len(s):
                result.append(current.copy())
                return

            # Try every possible substring beginning at start
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                # Only choose the substring if it is a palindrome
                if is_palindrome(substring):
                    current.append(substring)

                    # Partition the remaining part of the string
                    backtrack(end + 1, current)

                    # Undo the choice
                    current.pop()

        backtrack(0, [])

        return result