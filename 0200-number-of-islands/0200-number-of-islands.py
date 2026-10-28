class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        islands = 0

        def bfs(r,c):
            visit.add((r,c))
            q = deque()
            q.append((r,c))
            
            while q:
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                row, col = q.popleft()

                for rw, cl in directions:
                    r = row+rw
                    c = col+cl
                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == '1' and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))


        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands