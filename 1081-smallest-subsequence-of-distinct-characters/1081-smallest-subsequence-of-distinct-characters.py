class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {}

        # Store the last index of every character
        for index, char in enumerate(s):
            last_occurrence[char] = index

        stack = []
        in_stack = set()

        for index, char in enumerate(s):

            # Do not add a duplicate character
            if char in in_stack:
                continue

            # Remove larger characters when they occur again later
            while (
                stack
                and stack[-1] > char
                and last_occurrence[stack[-1]] > index
            ):
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)