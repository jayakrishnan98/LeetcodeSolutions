class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        
        # Count frequencies
        for num in nums:
            freq[num] += 1
        
        # Prefix sum
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(freq[num - 1])
        
        return result