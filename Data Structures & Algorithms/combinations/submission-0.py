class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        def new(start, cur):
            if len(cur) == k:
                result.append(cur.copy())
                return

            for i in range(start, n + 1):
                cur.append(i)
                new(i+1, cur)
                cur.pop()
        
        new(1, [])

        return result