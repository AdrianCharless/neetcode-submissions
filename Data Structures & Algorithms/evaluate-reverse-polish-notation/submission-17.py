class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+" or tok == "*" or tok == "-" or tok == "/":
                arg2 = stack.pop()
                arg1 = stack.pop()
                sum12 = 0
                prod12 = 1   
                if tok == "+":
                    stack.append(arg2 + arg1)
                elif tok == "*":
                    stack.append(arg2 * arg1)
                elif tok == "-":
                    stack.append(arg1 - arg2)
                elif tok == "/":
                    stack.append(int(arg1 / arg2))
                else:
                    return 0
            else:
                stack.append(int(tok))
        return int(stack[-1])

            