class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(new_str) - 1

        while l <= r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True