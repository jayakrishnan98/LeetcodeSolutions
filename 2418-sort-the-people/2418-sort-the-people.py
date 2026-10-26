class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = list(zip(heights, names))
        people.sort(key=lambda x: x[0], reverse=True)
        return [name for height, name in people]