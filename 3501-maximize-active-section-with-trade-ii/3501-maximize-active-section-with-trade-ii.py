from typing import List
from bisect import bisect_left, bisect_right


class SegmentTree:
    def __init__(self, values):
        self.size = 1

        while self.size < len(values):
            self.size *= 2

        self.tree = [0] * (2 * self.size)

        # Place values in the leaf nodes
        for index in range(len(values)):
            self.tree[self.size + index] = values[index]

        # Build the tree
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = max(
                self.tree[2 * index],
                self.tree[2 * index + 1]
            )

    def query(self, left, right):
        """
        Return the maximum value from left to right, inclusive.
        """

        if left > right:
            return 0

        left += self.size
        right += self.size

        result = 0

        while left <= right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1

            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        total_ones = s.count("1")

        zero_starts = []
        zero_ends = []
        zero_lengths = []

        index = 0

        # Find every consecutive zero block
        while index < len(s):
            if s[index] == "1":
                index += 1
                continue

            start = index

            while index < len(s) and s[index] == "0":
                index += 1

            end = index - 1

            zero_starts.append(start)
            zero_ends.append(end)
            zero_lengths.append(end - start + 1)

        # adjacent_sums[i] represents:
        # zero_lengths[i] + zero_lengths[i + 1]
        adjacent_sums = []

        for index in range(len(zero_lengths) - 1):
            current_sum = (
                zero_lengths[index]
                + zero_lengths[index + 1]
            )

            adjacent_sums.append(current_sum)

        segment_tree = SegmentTree(adjacent_sums)

        answers = []

        for left, right in queries:

            # First zero block whose ending position is >= left
            first_group = bisect_left(zero_ends, left)

            # Last zero block whose starting position is <= right
            last_group = bisect_right(zero_starts, right) - 1

            maximum_gain = 0

            # At least two zero blocks must exist inside the query
            if first_group < last_group:

                first_length = (
                    zero_ends[first_group]
                    - max(zero_starts[first_group], left)
                    + 1
                )

                last_length = (
                    min(zero_ends[last_group], right)
                    - zero_starts[last_group]
                    + 1
                )

                # Exactly two zero blocks intersect the query
                if first_group + 1 == last_group:
                    maximum_gain = first_length + last_length

                else:
                    # Pair containing the partially included first block
                    first_pair_gain = (
                        first_length
                        + zero_lengths[first_group + 1]
                    )

                    # Pair containing the partially included last block
                    last_pair_gain = (
                        zero_lengths[last_group - 1]
                        + last_length
                    )

                    maximum_gain = max(
                        first_pair_gain,
                        last_pair_gain
                    )

                    # Pairs made from completely included zero blocks
                    internal_left = first_group + 1
                    internal_right = last_group - 2

                    if internal_left <= internal_right:
                        internal_gain = segment_tree.query(
                            internal_left,
                            internal_right
                        )

                        maximum_gain = max(
                            maximum_gain,
                            internal_gain
                        )

            answers.append(total_ones + maximum_gain)

        return answers