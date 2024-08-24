class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operator:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == '+':
                    res = operand_1 + operand_2
                elif token == '-':
                    res = operand_1 - operand_2
                elif token == '*':
                    res = operand_1 * operand_2
                else:
                    res = int(operand_1 / operand_2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
