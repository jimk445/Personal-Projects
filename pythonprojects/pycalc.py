#local identification, sys importing, and opening message
version = 1.1
print(f'Welcome to PYCALC v{version}!')
print('Recent changes:')
print('negative number support')
print('-------------------------------')
import sys
operator = input('enter an operator(+ - * /): ')
num1 = (input('enter first number: '))
num2 = (input('enter second number: '))

#detect if numbers are actually numbers
if num1.removeprefix("-").isdigit():
    num1 = float(num1)
else:
    print(f'exiting, "{num1}" is not a number.')
    sys.exit(1)

if num2.removeprefix("-").isdigit():
    num2 = float(num2)
else:
    print(f'exiting, "{num2}" is not a number.')
    sys.exit(2)
    
#calculate & invalid operator crash
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f'exiting, "{operator}" is an invalid operator, only the following are valid: + - * /')
    sys.exit(3)
