class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs: 
            l = len(string)
            s += str(l) + "#" + string

        return s

    def decode(self, s: str) -> List[str]:

        i = 0
        strings = []

        while i < len(s):
            
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strings.append(s[i:j])
            i = j

        return strings