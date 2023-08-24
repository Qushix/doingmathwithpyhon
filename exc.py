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

    ####################################################### 20. PAGE

    print("Change")