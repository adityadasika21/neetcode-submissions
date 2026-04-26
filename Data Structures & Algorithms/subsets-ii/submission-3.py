class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(i, subsets): 
            res.append(subsets[::])

            for j in range(i, len(nums)): 
                if j > i and nums[j] == nums[j -1]:
                    continue

                subsets.append(nums[j])
                backtrack(j + 1, subsets)
                subsets.pop()

        backtrack(0, [])

        return res