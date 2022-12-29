def isBalanced(s):
    s = s.split(",")
    s = "".join(s)
    s = s.split()[0]
    stack = []
    print(s)
    print()

    for c in s:
        print(stack)
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return "NO"
            else:
                stack = stack[:-1]
        elif c == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return "NO"
            else:
                stack = stack[:-1]
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return "NO"
            else:
                stack = stack[:-1]
    print(stack)
    return "YES" if len(stack) == 0 else "NO"


# t = int(input())

# for _ in range(t):
    # s = input()
    # print(isBalanced(s))

s = "{[()]}"
# s = "{[(])}"
# s = "{{[[(())]]}}"

print(isBalanced(s))