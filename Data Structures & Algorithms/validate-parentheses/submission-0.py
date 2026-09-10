class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_to = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in open_to:
                if not (stack and stack.pop() == open_to[c]):
                    return False
            else:
                stack.append(c)

        return not stack