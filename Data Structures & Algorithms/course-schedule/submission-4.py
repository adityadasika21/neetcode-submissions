class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
            indegree[pre] += 1

        q = deque([ i for i in range(numCourses) if indegree[i] == 0 ])
        finish = 0

        while q: 
            curCrs = q.popleft()
            finish += 1

            for pre in preMap[curCrs]:
                indegree[pre] -= 1
                if indegree[pre] == 0: 
                    q.append(pre)

        return finish == numCourses