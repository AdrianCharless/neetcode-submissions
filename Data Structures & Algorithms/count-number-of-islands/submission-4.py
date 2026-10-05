class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < len(grid)) and (nc >= 0 and nc < len(grid[0])):
                        if grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))



        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
                    
        
        return islands

