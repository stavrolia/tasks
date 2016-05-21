stack =[]
for symbol in input().split():
    if symbol == '+':
        stack.append(stack.pop() + stack.pop())
    elif symbol == '-':
        stack.append(- stack.pop() + stack.pop())
    elif symbol == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(symbol))
print(stack.pop())
