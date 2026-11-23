class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        if not stones:
            return 0
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            num1 = -heapq.heappop(heap)
            num2 = -heapq.heappop(heap)
            if num2 < num1:
                res = num1 - num2
                heapq.heappush(heap, -res)
            if not heap:
                return 0
        return -heap[0]


