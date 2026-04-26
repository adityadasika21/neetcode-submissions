class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != (n - 1) :
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque()

        q.append([0, -1])
        visit.add(0)
        par = -1
        while q: 
            for _ in range(len(q)):

                cur, par = q.popleft()

                for nei in adj[cur]:
                    if nei == par: 
                        continue 
                    if nei in visit: 
                        return False 
                    q.append([nei, cur])
                    visit.add(nei)
                

        return len(visit) == n