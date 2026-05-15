class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for letter in s:
            if not (letter.isalnum()):
                s = s.replace(letter, "")
            
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
