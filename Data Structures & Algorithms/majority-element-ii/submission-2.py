class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #boyer moore
        candidate1 = 0
        candidate2 = 0
        count1 = 0
        count2 = 0
        threshold = len(nums) // 3
        result = []

        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        if nums.count(candidate1) > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > threshold:
            result.append(candidate2)
        return result





        # final_res = set()
        # threshold = len(nums) // 3
        # count = {}

        # for n in nums:
        #     if n not in count:
        #         count[n] = 1
        #     else:
        #         count[n] += 1
        #     if count[n] > threshold:
        #         final_res.add(n)
        # return list(final_res)

            
