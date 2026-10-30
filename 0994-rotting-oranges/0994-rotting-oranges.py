class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        result = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append((r,c))
                    fresh -= 1
            result += 1
        
        return result if fresh==0 else -1