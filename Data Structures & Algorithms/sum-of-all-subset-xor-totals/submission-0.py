class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, final_xor):
            if i == len(nums):
                return final_xor
            
            include = dfs(i + 1, final_xor)
            skip = dfs(i + 1, final_xor ^ nums[i])
        
            return include + skip 
                    
        return dfs(0, 0)
