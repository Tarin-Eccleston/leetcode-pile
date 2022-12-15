class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []

        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{' ):
                paren_stack.append(s[i])
            else:
                if (len(paren_stack) < 1):
                    return False

                if (paren_stack[len(paren_stack)-1] == '(' and s[i] == ')'):
                    paren_stack.pop()
                elif (paren_stack[len(paren_stack)-1] == '[' and s[i] == ']'):
                    paren_stack.pop()
                elif (paren_stack[len(paren_stack)-1] == '{' and s[i] == '}'):
                    paren_stack.pop()
                else:
                    return False

        if (len(paren_stack) == 0):
            return True
        else:
            return False