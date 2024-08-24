class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = ['(']

        def backtrack(openN, closeN):
            if openN == n and closeN == n:
                result.append(''.join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(1, 0)
        return result
