class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import math, heapq
        dists = []
        def dist(x, y):
            return math.sqrt(x*x + y*y)
        q = heapq
        for x, y in points:
            dxy = dist(x, y)
            dists.append((dxy, [x, y]))

        heapq.heapify(dists)
        res = [] 
        while len(res) < k:
            dist, coord = heapq.heappop(dists)
            res.append(coord)

        return res
        