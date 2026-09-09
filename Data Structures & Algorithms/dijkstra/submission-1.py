class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adjList = {i : [] for i in range(n)}

        for s, d, w in edges: 
            adjList[s].append([d, w])


        shortest = {}

        minHeap = [[0, src]]

        while minHeap: 

            w1, d1 = heapq.heappop(minHeap)
            if d1 in shortest: 
                continue
            
            shortest[d1] = w1

            for d2, w2 in adjList[d1]:
                if d2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, d2])

        for i in range(n): 
            if i not in shortest: 
                shortest[i] = -1

        return shortest