class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = [0] * len(graph)

        def bfs(i):
            if group[i]:
                return True
            q = deque([i])
            group[i] = -1
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if group[nei] == group[i]:
                        return False
                    else:
                        q.append(nei)
                        group[nei] = -1 * group[i]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True
