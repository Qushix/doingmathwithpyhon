import math
import sympy as sp
from sympy.core.sympify import SympifyError

if __name__ == '__main__':
    '''
    theta = sp.Symbol('theta')
    eq = sp.sin(theta) + sp.sin(theta)
    print(eq)
    '''

    '''
    u, t, g, theta = sp.symbols('u, t, g, theta')
    eq = u*sp.sin(theta) - g*t
    sol = sp.solve(eq, t)
    print(sol[0])
    '''

    '''
    x = sp.Symbol('x', positive=True)
    if (x+5) > 0:
        print('Do something')
    else:
        print('Do something else')
    '''

    '''
    x = sp.Symbol('x')
    eq = sp.Limit(sp.sin(x)/x, x, 0, dir='+')
    print(eq.doit())
    '''

    '''
    p, r, t, n = sp.symbols('p, r, t, n', positive=True)
    eq = sp.Limit(p*(1 + r/n)**(n*t), n, sp.S.Infinity, dir='-')
    sol = eq.doit()
    print(sol)
    '''

    '''
    t, t1, delta_t = sp.symbols('t, t1, delta_t')
    St = 5*t**2 + 2*t + 8
    St1 = St.subs({t: t1})
    St1_delta = St.subs({t: t1 + delta_t})

    eq = sp.Limit((St1_delta - St1) / delta_t, delta_t, 0)
    sol = eq.doit()
    print(sol)
    '''

    '''
    t = sp.Symbol('t')
    St = 5 * t ** 2 + 2 * t + 8
    eq = sp.Derivative(St, t)
    sol = eq.doit().subs({t: 1})
    print(sol)
    '''

    '''
    x = sp.Symbol('x')
    eq = (x**3 + x**2 + x) * (x**2 + x)
    sol = sp.Derivative(eq, x)
    print(sol.doit())
    '''

    '''
    def derivative(eq, param):
        sol = sp.Derivative(eq, param)
        print('Derivative:')
        sp.pprint(sol.doit())
        return sol.doit()

    def find_ext(eq):
        sol = sp.solve(eq)
        print('Your extreme value: {0}'.format(sol[0]))

    eq = input('Enter a function: ')
    param = input('Enter the variable to differentiate with respect to: ')
    try:
        eq = sp.sympify(eq)
    except SympifyError:
        print('Invalid input.')
    else:
        param = sp.Symbol(param)
        eq_to_ext = derivative(eq, param)
        find_ext(eq_to_ext)
    '''

    '''
    x = sp.Symbol('x')
    f = x**5 - 30*x**3 + 50*x
    d1 = sp.Derivative(f, x).doit()
    critical_points = sp.solve(d1)
    print(critical_points)

    d2 = sp.Derivative(f, x, 2).doit()

    A = critical_points[2]
    B = critical_points[0]
    C = critical_points[1]
    D = critical_points[3]

    print(d2.subs({x: B}).evalf())
    print(d2.subs({x:C}).evalf())
    print(d2.subs({x:A}).evalf())
    print(d2.subs({x:D}).evalf())
    '''

    def grad_ascent(x0, f1x, x):
        epsilon = 1e-6
        step_size = 1e-4
        x_old = x0
        x_new = x_old + step_size*f1x.subs({x: x_old}).evalf()
        while abs(x_old - x_new) > epsilon:
            x_old = x_new
            x_new = x_old + step_size * f1x.subs({x: x_old}).evalf()
        return x_new

    f = input('Enter a function with one variable: ')
    var = input('Enter the variable to differentiate with respect to: ')
    var0 = float(input('Enter the initial value of the variable: '))
    try:
        f = sp.sympify(f)
    except SympifyError:
        print('Invalid input.')
    else:
        var = sp.Symbol('val')
        f1 = sp.Derivative(f, var)
        var_max = grad_ascent(var0, f1, var)
        print('{0}: {1}'.format(var.name, var_max))
        print('Maximum value: {0}'.format(f.subs({var: var_max})))
