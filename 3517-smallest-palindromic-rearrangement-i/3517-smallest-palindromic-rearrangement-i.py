class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        my_arr = [0] * 26
        
        for item in s:
            my_arr[ord(item) - ord('a')] += 1
        result = ''
        mid = ''
        for i in range(len(my_arr)):
            while my_arr[i] > 1:
                result += chr(ord('a') + i)
                my_arr[i] -= 2
            if my_arr[i] == 1:
                mid = chr(ord('a') + i)
                my_arr[i] -= 1

        result = result + mid + result[::-1]

        return result

