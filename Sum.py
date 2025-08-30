a = int(input('Enter the first number: '))
print("Enter'+' for addition  \n   '-' for subtraction \n   'X' for multiplication \n  '/' for division") 
operation= input('Enter the operation here: ')
for i in range (3): 
    if operation not in ['+','-','X','/']:
        print('Invalid operation')
        operation = input('Enter the correct operation: ')  
   
b = int(input('Enter the second number: '))   
         

if operation == '+':
     print(a+b)
elif operation == '-':
     print(a-b)
elif operation == 'X':
     print(a*b)
elif operation == '/':
     print(a/b)
else:
     print('Invalid operation')