class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

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
        flat_index = 0
        for i in range(len(grid)):
            current = []
            j = 0
            while j < len(grid[0]):
                current.append(flattened[flat_index])
                j += 1
                flat_index += 1
            result.append(current)
          
        return result


