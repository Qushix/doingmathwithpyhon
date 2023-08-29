import sympy as sp
if __name__ == '__main__':
    '''
    x = sp.Symbol('x')
    print(x + x + 1)
    print(x.name)

    a, b, c = sp.symbols('a, b, c')
    print(a*a + b + b + c + 0.5*c)
    '''

    '''
    x, y = sp.symbols('x, y')
    expr = x**2 - y**2
    fact = sp.factor(expr)
    print(fact)
    expn = sp.expand(fact)
    print(expn)

    fact2 = (x + y)**5
    fact2_exp = sp.expand(fact2)
    print(fact2_exp)
    fact2_fact = sp.factor(fact2_exp)
    print(fact2_fact)

    sp.init_printing(order='rev-lex')
    sp.pprint(1 + 2*x - x*x)
    '''

    '''
    def print_series(n, value):
        sp.init_printing(order='rev-lex')
        x = sp.Symbol('x')
        series = x
        for i in range(2, n+1):
            series = series + x**i/i
        sp.pprint(series)
        res = series.subs({x: value})
        res = sp.simplify(res)
        sp.pprint(res)

    n = int(input('Enter the number of terms you want in series: '))
    value = float(input('Enter value: '))
    print_series(n, value)
    '''

    '''
    x, y = sp.symbols('s, y')
    expr = x**2 + 2*x*y + y**2
    res = expr.subs({x: 1-y})
    sp.simplify(res)
    print(sp.simplify(res))
    '''

