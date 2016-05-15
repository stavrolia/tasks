old_expression = input().split()
old_is_int = []
for i in old_expression:
    if i == '*' or i == '+' or i == '-':
        old_is_int.append(False)
    else:
        old_is_int.append(True)
new_expression = []
new_is_int = []
n = 0
while old_is_int != [True]:
    flag = [False, False]
    for i in range(len(old_is_int)):
        if flag[0] and flag[1]:
            flag[1] = False
        elif flag[0]:
            flag[0] = False
        else:
            if not old_is_int[i] or (old_is_int[i] and not old_is_int[i + 1]) or (old_is_int[i] and old_is_int[i + 1] and old_is_int[i + 2]):
                new_is_int.append(old_is_int[i])
                new_expression.append(old_expression[i])
            else:
                new_is_int.append(True)
                if old_expression[i + 2] == '*':
                    new_expression.append(int(old_expression[i]) * int(old_expression[i + 1]))
                elif old_expression[i + 2] == '+':
                    new_expression.append(int(old_expression[i]) + int(old_expression[i + 1]))
                elif old_expression[i + 2] == '-':
                    new_expression.append(int(old_expression[i]) - int(old_expression[i + 1]))
                flag = [True, True]

    old_is_int = new_is_int
    old_expression = new_expression
    new_is_int = []
    new_expression = []
print(int(old_expression[0]))
