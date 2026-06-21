class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        final_res = set()
        size = len(nums)
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
            if count[n] > size // 3:
                final_res.add(n)
        return list(final_res)

            
