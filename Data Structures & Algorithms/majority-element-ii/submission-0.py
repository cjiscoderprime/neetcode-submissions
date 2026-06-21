class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        final_res = set()
        size = len(nums)
        count = {}

        for n in nums:
            if n not in res:
                count[n] = 1
                res.append(n)
            else:
                count[n] += 1
            if count[n] > size // 3:
                final_res.add(n)
        return list(final_res)

            
