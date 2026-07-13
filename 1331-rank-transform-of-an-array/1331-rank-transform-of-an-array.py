class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        my_list = sorted(set(arr))
        rank = {
            value: index + 1 for index, value in enumerate(my_list)
        }
        print(rank)
        # Replace each value with its rank
        return [rank[value] for value in arr]