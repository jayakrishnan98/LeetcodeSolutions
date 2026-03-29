class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = set()
        result = []
        for num in nums1:
            if num not in freq:
                freq.add(num)

        for num in nums2:
            if num in freq:
                result.append(num)
                freq.remove(num)
        
        return result