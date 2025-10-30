import sys

def solution(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
        
    if len(stack) == 0:
        return True
    else:
        return False
    
        