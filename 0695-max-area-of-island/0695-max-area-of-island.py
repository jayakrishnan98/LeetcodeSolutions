class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            current_result = 1
            while q:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                row, col = q.popleft()
                
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                        current_result += 1
            return current_result

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    result = max(result, area)
    
        return result
        
