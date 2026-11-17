number1= input('Choose your first number: ')
operation= input('Choose the operation: ')
number2= input('Now another number: ')

def calculator(number1, operation,  number2):
    converted_number1= float(number1)
    converted_number2= float(number2)

    print(f'\n{converted_number1} {operation} {converted_number2} = \n')

    if operation== '+':
        result1= converted_number1 + converted_number2 
        print(f'The result of the sum is: {result1}')

    elif operation== '-':
        result2= converted_number1 - converted_number2
        print(f'The result of the substraction is: {result2}')

    elif operation== 'x':
        result3= converted_number1 * converted_number2
        print(f'The result of the multiplication is: {result3}')

    elif operation== '/':
        result4= converted_number1 / converted_number2
        print(f'The result of the division is: {result4}')
            
calculator(number1, operation, number2)