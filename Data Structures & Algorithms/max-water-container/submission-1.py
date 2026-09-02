class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        width = 0
        height = 0
        storage = 0
        max_storage = 0

        while l < r:
            width = r - l #indices
            height = min(heights[l], heights[r])
            storage = width * height

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_storage = max(max_storage, storage)
        return max_storage

            




