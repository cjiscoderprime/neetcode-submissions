class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1

       
        while l <= r:
            n = (l + r) // 2
            if target == nums[n]:
                return n

            if target > nums[n]:
                l = n + 1
            else:
                r = n - 1

        return l
