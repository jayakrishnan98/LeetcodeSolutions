class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for num in digits:
            a += str(num)
        b = int(a) + 1
        c = []
        for word in str(b):
            c.append(int(word))
        return c