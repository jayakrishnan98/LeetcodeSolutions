class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = 0
        maximum_gain = 0

        previous_zero_group = None

        index = 0

        while index < len(s):
            group_end = index

            # Find the end of the current group
            while (
                group_end < len(s)
                and s[group_end] == s[index]
            ):
                group_end += 1

            group_length = group_end - index

            if s[index] == "1":
                total_ones += group_length

            else:
                # Combine the current zero block with
                # the previous zero block
                if previous_zero_group is not None:
                    current_gain = (
                        previous_zero_group + group_length
                    )

                    maximum_gain = max(
                        maximum_gain,
                        current_gain
                    )

                previous_zero_group = group_length

            index = group_end

        return total_ones + maximum_gain