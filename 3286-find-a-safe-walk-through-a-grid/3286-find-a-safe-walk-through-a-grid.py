from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m = len(grid)
        n = len(grid[0])

        INF = float('inf')

        # dist[i][j] = minimum health lost to reach (i,j)
        dist = [[INF] * n for _ in range(m)]

        start_cost = grid[0][0]
        dist[0][0] = start_cost

        dq = deque()
        dq.append((0, 0))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:

            x, y = dq.popleft()

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:

                    new_cost = dist[x][y] + grid[nx][ny]

                    if new_cost < dist[nx][ny]:

                        dist[nx][ny] = new_cost

                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m-1][n-1] < health