class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = defaultdict(list)

        for src, dst in edges: 
            adjList[src].append(dst)
            adjList[dst].append(src)

        visit = set()

        def dfs(node):
            if node in visit: 
                return
            
            visit.add(node)
            
            for nei in adjList[node]: 
                dfs(nei)

        count = 0
        for i in range(n): 
            if i not in visit:
                dfs(i)
                count += 1
            
        return count