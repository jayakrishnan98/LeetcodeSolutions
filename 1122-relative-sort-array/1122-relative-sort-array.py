class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            freq[num] = 0
                
        for num in range(0, 1001):
            result.extend([num] * freq[num])

        return result