from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])

        flattened = []

        # Convert the 2D grid into a 1D list
        for row in grid:
            for value in row:
                flattened.append(value)

        total_elements = len(flattened)

        # Avoid unnecessary complete rotations
        k = k % total_elements

        # Shift the list to the right by k positions
        if k > 0:
            flattened = flattened[-k:] + flattened[:-k]

        result = []
        index = 0

        # Convert the shifted 1D list back into a 2D grid
        for row in range(rows):
            current_row = []

            for column in range(columns):
                current_row.append(flattened[index])
                index += 1

            result.append(current_row)

        return result