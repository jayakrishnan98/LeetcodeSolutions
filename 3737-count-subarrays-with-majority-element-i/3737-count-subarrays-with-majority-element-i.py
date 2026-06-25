class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for left in range(n):
            target_count = 0

            for right in range(left, n):
                if nums[right] == target:
                    target_count += 1

                length = right - left + 1

                if target_count > length / 2:
                    ans += 1

        return ans