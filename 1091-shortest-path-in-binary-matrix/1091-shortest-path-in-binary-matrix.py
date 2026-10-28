class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        visited = set((0,0))
        q = deque()
        q.append((0,0))
        count = 1

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return count
                for rw, cl in directions:
                    nr = r + rw
                    nc = c + cl
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            count +=1
        
        return -1