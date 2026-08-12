class Solution:
    def longestCommonSubsequence(
        self,
        text1: str,
        text2: str
    ) -> int:

        m = len(text1)
        n = len(text2)

        next_row = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            current_row = [0] * (n + 1)

            for j in range(n - 1, -1, -1):

                if text1[i] == text2[j]:
                    current_row[j] = 1 + next_row[j + 1]
                else:
                    current_row[j] = max(
                        next_row[j],
                        current_row[j + 1]
                    )

            next_row = current_row

        return next_row[0]