class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = { i : [] for i in range(numCourses)}

        for crs, pre in prerequisites: 
            adjList[crs].append(pre)

        visit, cycle = set(), set()

        result = []

        def dfs(crs): 

            if crs in cycle: 
                return False

            if crs in visit:
                return True

            cycle.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False: 
                return []

        return result