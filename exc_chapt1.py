from fractions import Fraction

if __name__ == "__main__":
    ####################################################### 0. PAGE
    # print(type(3))
    # print(int(float("3.0")))

    # f = Fraction(3, 4)
    # print(f)

    # a = 2 + 3j
    # b = 3 - 5j
    # print(a)
    # print(a + b)
    # print(a * b)
    # print(a / b)

    # print(a.real, a.imag)
    # print(a.conjugate())

    '''
    k = input('Input a float: ')
    print(float(k) + 1)

    m = float(input())
    print(m)
    '''

    '''
    try:
        a = float(input('Enter a number: '))
    except ValueError:
        print('You entered a invalid number')
    '''

    '''
    l = Fraction(input('Enter a fraction: '))
    print(float(l))
    '''

    '''
    try:
        a = Fraction(input('Enter a fraction: '))
    except ZeroDivisionError:
        print('Invalid fraction')
    '''

    '''
    def is_factor(a, b):
        if b % a == 0:
            return True
        else:
            return False
    
    p = is_factor(2, 7)
    print(p)
    '''

    '''
    def is_factor(n):
        for i in range(1, n+1, 1):
            if n % i == 0:
                print(i)
            else:
                continue
    n = float(input('Enter your number: '))
    if n > 0 and n.is_integer():
        is_factor(int(n))
    else:
        print('Input a correct integer!')
    '''

    '''
    def multiplication(n):
        for i in range(1, 11):
            print('{0} x {1} = {2}'.format(n, i, n*i))
    u = float(input('Enter a number for multiplication: '))
    if u > 0 and u.is_integer():
        multiplication(u)
    else:
        print('Input a correct number!')
    '''

    # print("{0:.2f}".format(1.3256))
    '''
    def print_menu():
        print('1. Kilometers to miles')
        print('2. Miles to kilometers')
    def km_miles():
        km = float(input('Enter distance in kilometers: '))
        miles = km / 1.609
        print('Distance in miles: {0}'.format(miles))
    def miles_km():
        miles = float(input('Enter distance in miles: '))
        km = miles * 1.609
        print('Distance in kilometers: {0}'. format(km))

    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    elif choice == '2':
        miles_km()
    else:
        print('Option not found...')
    '''
    ####################################################### 20. PAGE
    '''
    def roots(a, b, c):
        D = (b**2 - 4*a*c)**0.5
        x_1 = (-b + D) / (2*a)
        x_2 = (-b - D) / (2*a)

        print('x1 = {0}'.format(x_1))
        print('x2 = {0}'.format(x_2))

    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")

    roots(float(a), float(b), float(c))
    '''

    # Even-odd vending machine
    '''
    def even_odd(x):
        if x % 2 == 0:
            print("Even.")
            row_x = []
            for i in range(x, 19 + x, 2):
                row_x.append(i)
            print(row_x)
        else:
            print("Odd.")
            row_x = []
            for i in range(x, 19 + x, 2):
                row_x.append(i)
            print(row_x)

    try:
        x = float(input("Enter an integer: "))
        if x.is_integer():
            even_odd(int(x))
        else:
            print("Enter an integer!")
    except ValueError:
        print("Enter a correct number!")
    '''
    # Enhanced multiplication table generator
    '''
    def enh_mult_tabl(x, n):
        for i in range(1, n + 1):
            print("{0} x {1} = {2}".format(x, i, x*i))
    x = float(input("Enter a main number: "))
    n = float(input("Enter an multiplicator range: "))
    if x.is_integer() and n.is_integer():
        enh_mult_tabl(int(x), int(n))
    else:
        print("Numbers aren't integers!")
    '''

    '''
    # Enhanced unit converter
    def main_menu():
        print("1. Mass converter.")
        print("2. Temperature converter.")


    def second_menu(choice_1):
        if choice_1 == 1:
            print("1. Kilograms to pounds.")
            print("2. Pounds to kilograms.")
        elif choice_1 == 2:
            print("1. Kelwins to celsius.")
            print("2. Celsius to kelwins.")
        else:
            print("Option not found.")


    def program(x, choice_1, choice_2):
        if choice_1 == 1 and choice_2 == 1:
            value = x * 2.2046
            print("{0} kg equals {1:.4f} lbs".format(x, value))

        elif choice_1 == 1 and choice_2 == 2:
            value = x / 2.2046
            print("{0} lbs equals {1:.4f} kg".format(x, value))

        elif choice_1 == 2 and choice_2 == 1:
            value = x - 273.15

            print("{0} K equals {1} degC".format(x, value))
        elif choice_1 == 2 and choice_2 == 2:
            value = x + 273.15
            print("{0} degC equals {1} K".format(x, value))

    while True:
        main_menu()
        choice_1 = float(input("Enter the number of your program: "))
        second_menu(choice_1)
        choice_2 = float(input("Enter the number of your program: "))
        x = float(input("Enter a value which will be converted: "))
        program(x, choice_1, choice_2)

        cont = input("Enter (y) if you want to continue: ")
        if cont == "y":
            break
    '''

    '''
    def fract(x_1, x_2, Operation):
        if Operation == "Add":
            print("Result: {0}".format(x_1 + x_2))
        elif Operation == "Subtract":
            print("Result: {0}".format(x_1 - x_2))
        elif Operation == "Divide":
            print("Result: {0}".format(x_1 / x_2))
        elif Operation == "Multiply":
            print("Result: {0}".format(x_1 * x_2))

    x_1 = Fraction(input("Input first fraction: "))
    x_2 = Fraction(input("Input second fraction: "))
    Operation = input("Choose your operation: Add, Subtract, Divide, Multiply: ")

    fract(x_1, x_2, Operation)
    '''

        ####################################################### 26. PAGE
