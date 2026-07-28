class Solution:
    def smallestPalindrome(self, s: str) -> str:
        frequency = [0] * 26

        for char in s:
            frequency[ord(char) - ord("a")] += 1

        left_parts = []
        middle = ""

        for index, count in enumerate(frequency):
            char = chr(ord("a") + index)

            # Put half of this character's copies on the left.
            left_parts.append(char * (count // 2))

            # A palindrome can have one odd-frequency character.
            if count % 2 == 1:
                middle = char

        left = "".join(left_parts)

        return left + middle + left[::-1]