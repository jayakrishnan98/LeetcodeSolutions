class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(range(len(indices)))
        for i in range(len(s)):
            a[indices[i]] = s[i]
        return ''.join(a)