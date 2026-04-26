class Solution:
    def romanToInt(self, s: str) -> int:
        
        number_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        count = 0
        for i in range(len(s)):
            if i+1 < len(s) and number_map[s[i]] < number_map[s[i + 1]]:
                count -= number_map[s[i]]
            else : 
                count += number_map[s[i]]

        return count