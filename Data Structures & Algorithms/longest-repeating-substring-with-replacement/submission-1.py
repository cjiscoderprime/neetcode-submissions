class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = set()
        l = 0
        res = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while (r - l + 1) - max(freq.values()) > k: #invalid window
                freq[s[l]] -= 1
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res