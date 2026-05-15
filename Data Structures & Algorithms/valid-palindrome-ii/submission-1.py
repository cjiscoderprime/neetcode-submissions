class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            elif s[l + 1] == s[r]:
                r-=1
            elif s[r - 1] == s[l]:
                l+=1
            else:
                return False
        return True

                 
        