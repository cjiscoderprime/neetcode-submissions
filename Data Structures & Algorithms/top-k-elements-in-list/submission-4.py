class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        heap = []
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for number, count in freq.items():
            heapq.heappush(heap, (count, number))

            if len(heap) > k:
                heapq.heappop(heap)

        return [number for count, number in heap]
