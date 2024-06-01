def add(n1,n2):
    return n1+n2
    
def sub(n1,n2):
    return n1-n2
    
def mul(n1,n2):
    return n1*n2
    
def div(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Error! Division by zero attempt!"

while True:
    print('**Select which operation you want to perform.**\n1.)Addition\n2.)Subtraction\n3.)Multiplication\n4.)Division\n')

    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    select=int(input("Select an operation from 1, 2, 3, 4: "))

    if select == 1:
        print(add(num1,num2))

    elif select == 2:
        print(sub(num1,num2))

    elif select == 3:
        print(mul(num1,num2))

    elif select == 4:
        print(div(num1,num2))

    else:
        print('Select from 1 to 4')

    repeat = input("Do you want to repeat the operation? ")
    if repeat != 'yes':
        break