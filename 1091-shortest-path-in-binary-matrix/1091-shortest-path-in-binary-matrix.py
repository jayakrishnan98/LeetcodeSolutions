class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]

        q = deque([(0, 0)])
        visited = {(0, 0)}
        count = 1

        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                if cr == ROWS - 1 and cc == COLS - 1:
                    return count
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            count += 1

        return -1