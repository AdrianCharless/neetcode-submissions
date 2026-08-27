class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l == "[":
                stack.append("]")
            elif l == "{":
                stack.append("}")
            elif l == "(":
                stack.append(")")
            elif l == "]" or l == "}" or l == ")":
                if stack == []:
                    return False
                close = stack.pop()
                if close != l:
                    return False
        if stack == []:
            return True
        else:
            return False
            