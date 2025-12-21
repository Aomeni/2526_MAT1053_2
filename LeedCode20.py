class Solution(object):
    def isValid(self, s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pair:          
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:                 
                stack.append(ch)

        return not stack