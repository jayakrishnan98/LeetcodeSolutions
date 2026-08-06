class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        
        first = 0
        second = 1

        for i in range(n-1):
            current_sum = first + second
            first, second = second, current_sum
        return second