class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]

        # implementation without split()

        i = 0
        n = len(s)

        result = []

        while i < n:

            # skipping spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            
            j = i

            while j<n and s[j] != ' ':
                j += 1

            word = s[i:j][::-1]
            result.append(word)

            i = j
        
        return " ".join(result)
            
