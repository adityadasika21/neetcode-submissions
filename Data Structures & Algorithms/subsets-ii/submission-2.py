class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subTree, curset = [] , []
        self.helper(0, nums, curset, subTree)
        return subTree

    def helper(self, i, nums, curset, subTree ):
        if i == len(nums):
            subTree.append(curset.copy())
            return 

        curset.append(nums[i])
        self.helper(i+1, nums, curset, subTree)

        curset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i +=1

        self.helper(i+1, nums, curset, subTree)

        