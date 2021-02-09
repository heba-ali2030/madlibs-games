#simple calculator
num1= input('first num : ')
operation= input('operation : ')
num2= input('other num : ')

if operation == '+': 
    print(int(num1) + int(num2))
elif operation == '-': 
    print(int(num1) - int(num2))
elif operation == '*': 
    print(int(num1) * int(num2))
elif operation == '/' : 
    print(int(num1) / int(num2))
else:
    print(' I am a calculator not your mind reader, please restart me and be careful we have alot of responsabilities and many debits')


