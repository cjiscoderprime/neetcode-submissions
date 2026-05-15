class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        finalset = set()

        for n in nums:
            if n in finalset:
                return True
            finalset.add(n)
        
        return False
        