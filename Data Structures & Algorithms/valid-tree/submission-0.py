class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)> (n -1) : 
            return False

        adjList = [[] for _ in range(n)]

        for u,v in edges: 
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()

        def dfs(root, par): 
            if root in visit: 
                return False 

            visit.add(root)

            for nei in adjList[root]: 
                if nei == par: 
                    continue
                if not dfs(nei, root):
                    return False

            return True

        return dfs(0, -1) and len(visit )== n
