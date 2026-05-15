class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_str = " ".join(ch for ch in s if ch.isalnum()).lower()
        l, r = 0, len(result_str) - 1

        while l < r:
            if result_str[l] == result_str[r]:
                l+=1
                r-=1
            else:
                return False
        return True