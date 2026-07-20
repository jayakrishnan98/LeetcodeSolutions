from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])

        flattened = []

        for row in grid:
            for value in row:
                flattened.append(value)

        total_elements = len(flattened)

        k = k % total_elements

        if k > 0:
            flattened = flattened[-k:] + flattened[:-k]

        result = []
        index = 0

        for row in range(rows):
            current_row = []

            for column in range(columns):
                current_row.append(flattened[index])
                index += 1

            result.append(current_row)

        return result