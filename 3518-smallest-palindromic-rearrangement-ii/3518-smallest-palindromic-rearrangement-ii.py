class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_length = n // 2

        # Because s is already a palindrome, its first half contains
        # exactly one character from every matching pair.
        frequency = [0] * 26

        for char in s[:half_length]:
            index = ord(char) - ord("a")
            frequency[index] += 1

        middle = s[half_length] if n % 2 == 1 else ""

        # Required by the problem statement.
        prelunthak = (s, k)
        limit = prelunthak[1]

        # Check whether k palindromic permutations exist.
        total_permutations = self.countPermutations(frequency, limit)

        if total_permutations < k:
            return ""

        left = []

        # Construct the k-th smallest left half.
        for _ in range(half_length):

            for index in range(26):
                if frequency[index] == 0:
                    continue

                # Temporarily choose this character.
                frequency[index] -= 1

                permutations = self.countPermutations(frequency, k)

                if permutations >= k:
                    # The answer is inside this group.
                    left.append(chr(ord("a") + index))
                    break

                # Skip this entire group.
                k -= permutations
                frequency[index] += 1

        left_half = "".join(left)

        return left_half + middle + left_half[::-1]

    def countPermutations(self, frequency, limit):
        remaining = sum(frequency)
        ways = 1

        for count in frequency:
            if count == 0:
                continue

            # We only need to know whether ways reaches limit.
            required = (limit + ways - 1) // ways

            ways *= self.combination(
                remaining,
                count,
                required
            )

            if ways >= limit:
                return limit

            remaining -= count

        return ways

    def combination(self, n, r, limit):
        r = min(r, n - r)
        result = 1

        for i in range(1, r + 1):
            result = result * (n - r + i) // i

            if result >= limit:
                return limit

        return result