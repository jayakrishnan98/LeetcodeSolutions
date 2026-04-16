class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res
        
        freq = [0] * 26
        
        # Build frequency map for p
        for c in p:
            freq[ord(c) - ord('a')] += 1
        
        left = 0
        count = len(p)
        
        for right in range(len(s)):
            # If current char is needed, decrease count
            if freq[ord(s[right]) - ord('a')] > 0:
                count -= 1
            
            # Decrease freq (we are using this char)
            freq[ord(s[right]) - ord('a')] -= 1
            
            # If window size exceeds p, move left
            if right - left + 1 > len(p):
                # If left char was useful, restore count
                if freq[ord(s[left]) - ord('a')] >= 0:
                    count += 1
                
                freq[ord(s[left]) - ord('a')] += 1
                left += 1
            
            # If all chars matched
            if count == 0:
                res.append(left)
        
        return res