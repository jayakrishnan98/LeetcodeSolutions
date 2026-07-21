class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count("1")
        zero_groups = []

        index = 0

        while index < len(s):
            if s[index] == "1":
                index += 1
                continue

            # We found the beginning of a zero block
            zero_count = 0

            while index < len(s) and s[index] == "0":
                zero_count += 1
                index += 1

            zero_groups.append(zero_count)

        maximum_gain = 0

        # Check every pair of neighbouring zero blocks
        for index in range(len(zero_groups) - 1):
            current_gain = zero_groups[index] + zero_groups[index + 1]
            maximum_gain = max(maximum_gain, current_gain)

        return total_ones + maximum_gain