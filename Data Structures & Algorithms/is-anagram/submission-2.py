class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        freq1 = {}      
        freq2 = {}

        for s in str1:
            if s in freq1:
                freq1[s] += 1
            else:
                freq1[s] = 1
        
        for t in str2:
            if t in freq2:
                freq2[t] += 1
            else:
                freq2[t] = 1
            
        return(freq1 == freq2)