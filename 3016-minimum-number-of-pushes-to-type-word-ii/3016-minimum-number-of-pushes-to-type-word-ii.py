class Solution:
    def minimumPushes(self, words: str) -> int:
        
        frequency = [0] * 26

        for word in words:
            frequency[ord(word) - ord('a')] += 1

        frequency.sort(reverse=True)
        result = 0
        for i in range(len(frequency)):
            result += frequency[i] * ((i//8) + 1)

        return result

        