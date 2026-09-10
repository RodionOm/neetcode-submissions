class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for symb in s:
            if symb.isalnum():
                newS += symb.lower()
        return newS == newS[::-1]