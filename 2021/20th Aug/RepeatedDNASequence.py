class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sub_strings = {}
        result = []
        sub_string = s[0:10]
        
        for i in range(10, len(s)+1):
            
            if sub_string not in sub_strings:
                sub_strings[sub_string] = 1
            else:
                sub_strings[sub_string] += 1
                
            if i != len(s): sub_string = sub_string[1:]+ s[i]
            
        for j in sub_strings.keys():
            if sub_strings[j] > 1:
                result.append(j)
                
        return result 
        
