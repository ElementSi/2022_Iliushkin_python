request = input().split()
try:
    first_operand = int(request[0])
    operation = request[1]
    second_operand = int(request[2])
except:
    res = "Bad input"
else:
    if operation == '+':
        res = first_operand + second_operand
    elif operation == '-':
        res = first_operand - second_operand
    elif operation == '*':
        res = first_operand * second_operand
    elif operation == '^':
        res = first_operand ** second_operand
    else:
        res = "Bad input"

print(res)
