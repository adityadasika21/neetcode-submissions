class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_set = defaultdict(int)

        for c in s: 
            s_set[c] += 1

        t_set = defaultdict(int)
        for c in t: 
            t_set[c] +=1
            
        return s_set == t_set