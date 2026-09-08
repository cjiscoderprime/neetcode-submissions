class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        min_length = float("inf")

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                min_length = min(min_length, r - l + 1)
                window_sum -= nums[l]
                l += 1
        if min_length == float("inf"):
            return 0
        return min_length


