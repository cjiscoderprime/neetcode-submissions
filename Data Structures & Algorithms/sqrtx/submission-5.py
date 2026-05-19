class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while(l <= r):
            n = l + (r - l) // 2
            if n * n < x:
                l = n + 1
                res = n
            elif n * n > x:
                r = n - 1
            else:
                return n
        return res