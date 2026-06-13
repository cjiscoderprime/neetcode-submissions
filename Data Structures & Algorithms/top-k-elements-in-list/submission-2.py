class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        min_heap = []

        for number, count in frequency.items():
            heapq.heappush(min_heap, (count, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [number for count, number in min_heap]
        


