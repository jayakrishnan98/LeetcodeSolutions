class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        left, count = 0, len(s1)

        freq = [0] * 26

        for word in s1:
            freq[ord(word) - ord('a')] += 1 

        for right in range(len(s2)):
            if freq[ord(s2[right]) - ord('a')] > 0:
                count -= 1

            freq[ord(s2[right]) - ord('a')] -= 1

            if right - left + 1 > len(s1):
                if freq[ord(s2[left]) - ord('a')] >= 0:
                    count += 1
                
                freq[ord(s2[left]) - ord('a')] += 1
                left += 1

            if count == 0:
                return True

        return False