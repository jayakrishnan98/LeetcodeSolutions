class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(str(e) for e in digits))
        result = num + 1
        res = [int(i) for i in str(result)]
        return res
