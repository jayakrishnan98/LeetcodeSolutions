class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    q.append((row, col))
                    grid[row][col] = '0'
                
                    while q:
                        dr,dc = q.popleft()
                        for r,c in directions:
                            nr = r + dr
                            nc = c + dc

                            if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr,nc))
                    islands += 1
            
        return islands