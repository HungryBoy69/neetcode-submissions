class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['-', '+', '/', '*']
        stack = []
        for token in tokens:
            if token in operands:
                num1 = stack.pop()
                num2 = stack.pop()
                ans = eval(str(num2)+token+str(num1))
                print(ans)
                stack.append(int(ans))
            else:
                stack.append(token)
        print('the token value is', stack[-1])
        return int(stack[-1])