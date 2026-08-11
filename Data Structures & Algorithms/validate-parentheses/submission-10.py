class Solution:
    def isValid(self, s: str) -> bool:

        #Address edge cases
        if len(s) == None:
            return True
        if (len(s) % 2) == 1:
            return False

        stack = []
        for i in range (0, len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])
            if s[i] == '}' or s[i] == ']' or s[i] == ')':
                if len(stack) == 0:
                    return False
                if s[i] == '}':
                    if stack.pop() != '{':
                        return False
                if s[i] == ']':
                    if stack.pop() != '[':
                        return False
                if s[i] == ')':
                    if stack.pop() != '(':
                        return False
        

        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False

        
        