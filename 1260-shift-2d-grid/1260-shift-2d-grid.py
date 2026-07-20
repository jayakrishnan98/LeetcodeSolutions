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
        elif k>0:
            flattened = flattened[-k:] + flattened[:-k]

        result = []
        k = 0
        print(flattened)
        for i in range(len(grid)):
            current = []
            j = 0
            while j < len(grid[0]):
                current.append(flattened[k])
                j += 1
                k += 1
            result.append(current)
          
        return result


