class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)

        for word in strs:

            pattern = [0] * 26
            
            for letter in word:
                pattern[ord(letter) - ord('a')] += 1
            
            ans[tuple(pattern)].append(word)
        
        return list(ans.values())