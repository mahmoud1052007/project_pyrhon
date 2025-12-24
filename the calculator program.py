print('May the peace, mercy, and blessings of God be upon you. Welcome, my friend, to the calculator program. \n')
num1 = float(input('Enter first number: '))
oper = input('choose an operation(+,-,/,*,%) : ')
num2 = float(input('Enter second number: '))

if oper == '+':
    result = num1 + num2
    print(num1, '+', num2, '=', result)

elif oper == '-':
    result = num1 - num2
    print(num1, '-', num2, '=', result)

elif oper == '/':
    if num2 != 0:
        result = num1 / num2
        print(num1, '/', num2, '=', result)
    else:
        print("Can't divide by ZERO")

elif oper == '*':
    result = num1 * num2
    print(num1, '*', num2, '=', result)

elif oper == '%':
    result = num1 % num2
    print(num1, '%', num2, '=', result)

else:
    print('Invalid Operation')