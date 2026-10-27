class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            s,t = t,s
        s_counts = Counter(s)
        t_counts = Counter(t)

        for item, value in s_counts.items():
            if t_counts[item] != value:
                return False
        
        return True