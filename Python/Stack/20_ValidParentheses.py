class Solution:
    def isValid(self, s: str) -> bool:
        match_bracket = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for bracket in s:
            if bracket in match_bracket:
                stack.append(bracket)
            else:
                if not stack or match_bracket[stack.pop()] != bracket:
                    return False
        return not stack