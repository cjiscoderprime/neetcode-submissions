class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k+=1
            # else:
            #     k-=1
            #     nums[:k] == n
        return k