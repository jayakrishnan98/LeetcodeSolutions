class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        my_list = sorted(set(arr))
        rank = {
            value: index + 1 for index, value in enumerate(my_list)
        }
        # Replace each value with its rank
        return [rank[value] for value in arr]