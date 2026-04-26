class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = deque()
        visit = set()
        fresh = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 2: 
                    rotten.append([r, c])
                    visit.add((r, c))
                if grid[r][c] == 1: 
                    fresh += 1

        time = 0
        while rotten and fresh > 0: 
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in neighbors: 
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visit: 
                        rotten.append([nr, nc])
                        visit.add((nr, nc))
                        fresh -=1
            
            time += 1

        return time if fresh == 0 else -1