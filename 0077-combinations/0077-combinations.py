class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append(current.copy())
                return

            numbers_needed = k - len(current)
            last_possible_start = n - numbers_needed + 1

            for i in range(start, last_possible_start + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])

        return result