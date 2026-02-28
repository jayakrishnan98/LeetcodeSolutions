class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = list(jewels)
        out = 0
        for i in range(len(stones)):
            if stones[i] in a:
                out += 1
        return out