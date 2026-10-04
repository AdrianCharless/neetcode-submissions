class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        dirs = [[1,0], [0,-1], [-1,0], [0,1]]
        rotten = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        
        time = -1
        if fresh == 0:
            return 0
        q = deque(rotten)

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < len(grid)) and (nc >= 0 and nc < len(grid[0])):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            print(grid)
            time += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return time


