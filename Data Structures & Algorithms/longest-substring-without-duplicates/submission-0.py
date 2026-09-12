class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        know_c = set()

        for r, r_c in enumerate(s):
            while r_c in know_c:
                know_c.remove(s[l])
                l += 1
            know_c.add(r_c)
            res = max(res,r - l + 1)
        return res