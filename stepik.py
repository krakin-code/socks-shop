operation = input('What we do? ')
if operation not in ['+', '_', '*', '/']:
    exit('Error')
if operation == '/':
    ost = input('With ost?\n(Y)es or (N)o: ')
    ost = ost.upper()
first_number = int(input('First number: '))
second_number = int(input('Second number: '))
if operation == '+':
    print('Sum =', (first_number + second_number))
elif operation == '-':
    print('Pazn =', (first_number - second_number))
elif operation == '*':
    print('Proiz =', (first_number * second_number))
elif operation == '/':
    if ost == 'Y':
        print('Pajn =', (first_number / second_number))
    else:
        print('Pajn =', (first_number // second_number))

