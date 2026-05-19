"""
https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=string
"""

def valid_parentheses(string: str) -> bool:
    stack: list[str] = []
    pairs: dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
    for s in string:
        if s in pairs:
            if stack and stack[-1] == pairs[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    return not stack

brackets = "(([]))"
print("Input: ", brackets)
print("Output: ", valid_parentheses(brackets))