class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_pick = 0, 0
        freq = {}
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1

            max_pick = max(max_pick, right - left + 1)
        
        return max_pick