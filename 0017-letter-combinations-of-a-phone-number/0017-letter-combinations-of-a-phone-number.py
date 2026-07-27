class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current):
            if len(current) == len(digits):
                result.append("".join(current))
                return

            possible_letters = letters[digits[index]]
            for letter in possible_letters: 

                current.append(letter)

                backtrack(index + 1, current)

                current.pop()

        backtrack(0, [])
        return result