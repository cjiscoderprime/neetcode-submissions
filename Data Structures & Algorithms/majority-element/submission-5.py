class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsize = len(nums)
        occur = int(numsize/2)
        major_element = 0
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

            if freq[n] > occur:
                major_element = n
        return major_element
