#Simple Calculator
#By Yasmine Lopes
##################
##Ask which operation the user is going to do
##Ask for the first number
##Ask for the second number
##Calculate the operation
##Print the result
#Return to the calculator

while True:
    operation = input('Which of these operations you want to? \n(+, -, *, /) \nType here one of these symbols: ')
    num1 = int(input ('Ok, now type the first number: '))
    num2 = int(input ('Sure! Type the second number now: '))

    if operation == '+':
        total = num1 + num2
        print('Here is the total: ',total)
    elif operation == '-':
        total = num1 - num2
        print('Here is the total: ',total)
    elif operation == '*':
        total = num1 * num2
        print('Here is the total: ',total)
    elif operation == '/':
        total = num1 / num2
        print('Here is the total: ',total)
    else:
        print('Invalid Operation!!')