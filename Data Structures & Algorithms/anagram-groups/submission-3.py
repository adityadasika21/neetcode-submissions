class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for s in strs:
            value = [0] * 26
            for c in s: 
                value[ord('a') - ord(c)] += 1

            anagrams[str(value)].append(s)

        res = []

        for vaule in anagrams.values():
            res.append(vaule)

        return res