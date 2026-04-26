class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0, 1], [0, -1]]

        def bfs(i, j): 
            q = deque()
            grid[i][j] = '0'
            q.append((i,j))

            while q: 
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c 
                    if ( nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0') : 
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'


        res = 0
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == '1': 
                    bfs(r, c)
                    res+=1

        return res