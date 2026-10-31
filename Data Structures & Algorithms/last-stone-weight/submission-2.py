class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            if x < y:
                y = (y - x) * -1
                heapq.heappush(stones, y)
        if len(stones) == 0:
            return 0
        else:
            return stones[0] *-1


