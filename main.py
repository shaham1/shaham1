a = 1
b = 2
num1 = input('enter a number: ')
op = input('enter an operation: ')
num2 = input('enter another number: ')
Sum = float(num1) + float(num2)
difference = float(num1) - float(num2)
product = float(num1) * float(num2)
quotient = float(num1) / float(num2)
error_message = 'there is an error'

if op == '+':
    print(Sum)
elif op == '-':
    print(difference)
elif op == '*':
    print(product)
elif op == '/':
    print(quotient)
else:
    while a < b:
        print(error_message)
print(':)')
