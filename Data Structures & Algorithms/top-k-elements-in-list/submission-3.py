class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)
        
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: 
            freq_map[n] += 1
        for key, value in freq_map.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res
                    