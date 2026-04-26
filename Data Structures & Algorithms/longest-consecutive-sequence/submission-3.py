class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums: 
            curLength = 1
            while n+1 in numSet: 
                curLength += 1
                n+=1
            longest = max(longest, curLength)

        return longest