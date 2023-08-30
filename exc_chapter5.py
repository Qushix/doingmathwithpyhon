import sympy as sp
from fractions import Fraction
if __name__ == '__main__':
    '''
    s = sp.FiniteSet(2, 4, 6, Fraction(1, 5))
    print(s)
    q = 4 in s
    print(q)
    members = [1, 2, 3]
    test = sp.FiniteSet(*members)
    print(test)
    '''

    '''
    s = sp.FiniteSet(1, 2)
    t = sp.FiniteSet(1)
    q = t.is_subset(s)
    print(q)
    q2 = t.is_proper_subset(s)
    print(q2)
    '''

    '''
    s = sp.FiniteSet(1, 2, 3)
    t = sp.FiniteSet(3, 5, 6, 7)
    q1 = s.union(t)
    q2 = s.intersection(t)
    q3 = s * t
    print('Union: {0}'.format(q1))
    print('Intersection: {0}'.format(q2))
    print('Cartesian product: {0}'.format(q3))
    for element in q3:
        print(element)

    s_p = sp.FiniteSet(1, 2)
    for element in s_p**3:
        print(element)
    '''

    '''
    def time_period(L, g):
        T = 2*sp.pi*(L/g)**0.5
        return T

    L = sp.FiniteSet(15, 18, 21, 22.5, 25)
    g_values = sp.FiniteSet(9.8, 9.78, 9.83)
    print('{0:^20}{1:^20}{2:^20}'.format('Length [cm]', 'Gravity [m/s^2]', 'Time period [s]'))
    for element in L*g_values:
        l = element[0]
        g = element[1]
        t = time_period(l / 100, g)
        print('{0:^20}{1:^20}{2:^20.3f}'.format(float(l), float(g), float(t)))
    '''

    '''
    def propabilty(space, event):
        return len(event) / len(space)

    def check_prime(number):
        if number != 1:
            for element in range(2, number):
                if number % element == 0:
                    return False
        else:
            return False
        return True

    space = sp.FiniteSet(*range(1, 100))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = sp.FiniteSet(*primes)
    p = propabilty(space, event)
    print('Sample space: {0}'.format(space))
    print('Event: {0}'.format(event))
    print('Propability of rolling a prime: {0:.5}'.format(p))
    '''

