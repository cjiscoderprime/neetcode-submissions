class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        maxcount = 0


        for n in nums:
            if n - 1 not in res:
                count = 1
                current = n
                while current + 1 in res:
                    current += 1
                    count += 1
                maxcount = max(count, maxcount)
        return maxcount