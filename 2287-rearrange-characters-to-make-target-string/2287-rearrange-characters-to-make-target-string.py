class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        source_count = Counter(s)
        target_count = Counter(target)

        max_copies = float('inf')

        for char, required in target_count.items():
            available = source_count[char]
            copies = available // required

            max_copies = min(max_copies, copies)
        
        return max_copies