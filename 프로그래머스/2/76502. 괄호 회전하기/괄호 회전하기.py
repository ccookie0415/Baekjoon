def check(tokens):
    stack = []

    for token in tokens:
        if not stack:
            stack.append(token)
        elif stack:
            if token == '(' or token == '{' or token == '[':
                stack.append(token)
            elif token == '}' and stack[-1] == '{':
                stack.pop()
            elif token == ')' and stack[-1] == '(':
                stack.pop()
            elif token == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False

    return not stack

    
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if check(s[i:]+s[:i]) != False:
            answer += 1
    

    return answer