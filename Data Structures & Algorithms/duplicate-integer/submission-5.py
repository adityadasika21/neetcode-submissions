class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        checker = defaultdict(int)

        for n in nums: 
            if n in checker: 
                return True
            checker[n] += 1

        return False