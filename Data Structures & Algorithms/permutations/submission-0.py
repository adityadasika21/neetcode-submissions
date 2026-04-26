class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0: 
            return [[]]

        perms = self.permute(nums[1:])
        totalPerms = []
        for p in perms : 
            for j in range(len(p)+1):
                pCopy = p.copy()
                pCopy.insert(j, nums[0])
                totalPerms.append(pCopy)

        return totalPerms

    