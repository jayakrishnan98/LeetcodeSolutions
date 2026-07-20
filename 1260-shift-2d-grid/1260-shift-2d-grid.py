class Solution:
    def shiftGrid(
        self,
        grid: List[List[int]],
        k: int
    ) -> List[List[int]]:

        flattened = []

        for row in grid:
            for item in row:
                flattened.append(item)

        total_items = len(flattened)
        k = k % total_items

        if k == 0:
            return grid

        flattened = flattened[-k:] + flattened[:-k]

        result = []
        index = 0

        for i in range(len(grid)):
            current_row = []

            for j in range(len(grid[0])):
                current_row.append(flattened[index])
                index += 1

            result.append(current_row)

        return result