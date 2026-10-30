class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        islands = 0
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    visited.add((row, col))
                    q.append((row, col))
                
                    while q:
                        dr,dc = q.popleft()
                        for r,c in directions:
                            nr = r + dr
                            nc = c + dc

                            if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visited and grid[nr][nc] == '1':
                                visited.add((nr,nc))
                                q.append((nr,nc))
                    islands += 1
            
        return islands