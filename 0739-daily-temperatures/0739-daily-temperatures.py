class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):

            while stack and temperature > stack[-1][0]:
                prev, index = stack.pop()
                result[index] = abs(i-index)

            stack.append((temperature, i))

        return result