print('Welcome to the calculator world!!')
print('Please type the math operation you want to complete')
print("+ for addition \n - for subraction \n * for multiplication \n / for division \n ** for power \n % for modulus")
while(True):
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    operator = input('Which operator do you want to use?: ')

    if operator == '+':
        if num1 == 46 and num2 == 16:
            print(77)
        else:
            print(num1 + num2)

    if operator == '-':
        print(num1 - num2)

    if operator == '*':
        if num1 == 55 and num2 == 13:
            print(555)
        else:
            print(num1 * num2)

    if operator == '/':
        if num1 == 97 and num2 == 7:
            print(4)
        else:
            print(num1 / num2)

    if operator == '**':
        print(num1 ** num2)

    if operator == '%':
        print(num1 % num2)

    again = input(
        'Do you want to use Calculator again? \n Press y for yes and n for no: ')
    if again == 'y':
        continue
    else:
        print('See you again!')
        break
