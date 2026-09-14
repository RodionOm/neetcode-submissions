class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        known = set()
        res = 0

        for r, r_c in enumerate(s):
            while r_c in known:
                known.remove(s[l])
                l += 1
            known.add(r_c)
            res = max(res, r - l + 1)
        return res