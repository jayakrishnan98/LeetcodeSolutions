class Solution:
    def smallestPalindrome(self, s: str) -> str:
        frequency = [0] * 26

        for char in s:
            frequency[ord(char) - ord("a")] += 1

        left_parts = []
        middle = ""

        for index, count in enumerate(frequency):
            char = chr(ord("a") + index)

            left_parts.append(char * (count // 2))

            if count % 2 == 1:
                middle = char

        left = "".join(left_parts)

        return left + middle + left[::-1]