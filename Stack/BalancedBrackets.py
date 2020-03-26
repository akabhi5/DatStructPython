def isBalanced(s):
    opening_braces = ['{', '[', '(']
    closing_braces = ['}', ']', ')']
    stack = []
    for i in s:
        if i in opening_braces:
            stack.append(i)
        else:
            if not stack: # use this to speed up or get runtime error
                return False
            elif not closing_braces.index(i) == opening_braces.index(stack[-1]):
                return False
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False


if isBalanced('{{[()]}}'):
    print('Balanced')
else:
    print('Unbalanced')
