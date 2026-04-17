class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        left, res, count = 0, [], len(p)

        freq = [0] * 26

        for word in p:
            freq[ord(word) - ord('a')] += 1

        for right in range(len(s)):

            if freq[ord(s[right]) - ord('a')] > 0:
                count -= 1

            freq[ord(s[right]) - ord('a')] -= 1

            if (right - left +1) > len(p):
                if freq[ord(s[left]) - ord('a')] >= 0:
                    count += 1    
                freq[ord(s[left]) - ord('a')] += 1
                left += 1
            
            if count == 0:
                res.append(left)


        return res