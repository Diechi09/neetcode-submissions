class Solution:
    def isValid(self, s: str) -> bool:
        stuff = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            if c in stuff:
                if stack and stack[-1] == stuff[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False