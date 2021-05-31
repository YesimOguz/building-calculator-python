#this is a program that implements the functions of a calculator: addition,subtraction,multiplication,division and floor division.
#this is a calculator.

#get numbers from user
num1 = int(input('please enter a number: '))
num2 = int(input('please enter second number: '))

#ask user for the operation that she/he wants to perform on the numbers
operation = input('what would you like to do?(+,-,*/,//): ')

if operation == '*':
    result = num1*num2
    option = 'multiplication'
    

elif operation == '/':
    result = num1/num2
    option = 'division'
    

elif operation == '//':
    result =num1//num2
    option = 'floor division'
    

elif operation == '+':
    result = num1+num2
    option = 'addition'
    

elif operation == '-':
    result = num1-num2
    option = 'subtraction'

print(f'the result of {option} is {result}')







    


    
    


    

