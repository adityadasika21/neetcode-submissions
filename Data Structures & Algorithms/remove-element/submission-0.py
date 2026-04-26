class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        res = []

        for n in nums: 
            if n == val: 
                continue 
            res.append(n)
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)