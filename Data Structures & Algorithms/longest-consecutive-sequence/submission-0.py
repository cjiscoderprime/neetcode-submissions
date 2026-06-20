class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if (n - 1)  not in numset:
                next_num = 0
                while (n + next_num) in numset:
                    next_num += 1
                longest = max(longest, next_num)
        return longest