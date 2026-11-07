class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in range(len(s)):
            
            # if its an opening bracket push to the stack
            if s[i] == '[' or s[i] == '('  or s[i] == '{':
                stack.append(s[i])

            # if its a closing bracket, check if it matches the top
            elif s[i] == ']' or s[i] == ')'  or s[i] == '}':
                if len(stack) == 0:
                    return False

                if stack[-1] == '[' and s[i] == ']':
                    stack.pop()

                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()

                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()

                # they did not match, therefore not valid
                else:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True

    






