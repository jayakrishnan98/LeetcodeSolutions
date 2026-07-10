from typing import List


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # component[i] represents the connected component
        # containing node i.
        component = [0] * n

        component_id = 0

        for i in range(1, n):
            # A gap greater than maxDiff separates
            # this node from the previous component.
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1

            component[i] = component_id

        answer = []

        for u, v in queries:
            answer.append(component[u] == component[v])

        return answer