import sympy as sp
from sympy import SympifyError

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

    '''
    try:
        sp.init_printing(order='rev-lex')
        expr = input('Enter your expression: ')
        expr = sp.sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        sp.pprint(expr)
    '''

    '''
    def calc_prod(expr1, expr2):
        prod = sp.expand(expr1 * expr2)
        return prod

    try:
        expr1 = sp.sympify(input('Enter first expression: '))
        expr2 = sp.sympify(input('Enter second expression: '))
        x = sp.Symbol('x')
        product = calc_prod(expr1, expr2)
        product = sp.simplify(product)
        product = product.subs({x: 0.5})
        sp.pprint('Final expression: {0}'.format(product))
    except SympifyError:
        print('Invalid input.')
    '''

    '''
    x, y = sp.symbols('x, y')
    expr = [x**2 - 5 - 7 + y,
            x - 1.5*y]
    print(sp.solve(expr))
    '''

    '''
    x = sp.Symbol('x')
    expr = x**2 + x + 1
    res = sp.solve(expr, dict=True)
    print(res)
    '''

    '''
    x, a, b, c = sp.symbols('x, a, b, c')
    expr = a*x*x + b*x + c
    res = sp.solve(expr, x, dict=True)
    print(res)
    '''

    '''
    s, u, t, a = sp.symbols('s, u, t, a')
    expr = u*t + 0.5*a*t**2 - s
    res = sp.solve(expr, t, dict=True)
    result = res[0][t].subs({s: 20, u: 5, a: 1})
    sp.pprint(result)
    '''

    '''
    x, y = sp.symbols('x, y')
    expr1 = 2*x + 3*y - 6
    expr2 = 3*x + 2*y - 12
    res = sp.solve((expr1, expr2), dict=True)
    soln = res[0]
    print(soln)

    check1 = expr1.subs({x: soln[x],
                y: soln[y]})
    check2 = expr2.subs({x: soln[x],
                y: soln[y]})
    print(check1, check2)
    '''

    '''
    x = sp.Symbol('x')
    p = sp.plot((2*x + 3), (x, -5, 5), title="A line", xlabel='x', ylabel='2x + 3')
    p.save('line.png')
    '''

    '''
    def plot_expression(expr):
        y = sp.Symbol('y')
        solutions = sp.solve(expr, y)
        expr_y = solutions[0]
        sp.plot(expr_y)

    expr = input('Enter your expression in terms of x and y: ')

    try:
        expr = sp.sympify(expr)
    except SympifyError:
        print('Invalid input.')
    else:
        plot_expression(expr)
    '''

    '''
    x = sp.Symbol('x')
    p = sp.plot(2*x - 3, x**2 - 1, legend=True, show=False)
    p[0].line_color = 'b'
    p[1].line_color = 'r'
    p.show()
    '''

    # EXC 1

    '''
    def calc_Factor(expr):
        sol = sp.factor(expr)
        return sol
    try:
        expr = input('Enter your expression in term of x and y: ')
        expr = sp.sympify(expr)
    except SympifyError:
        print('Invalid input.')
    else:
        res = calc_Factor(expr)
        sp.pprint(res)
    '''

    # EXC 2
    '''
    def sp_plot(expr1, expr2, x, y):

        solution = sp.solve((expr1, expr2), dict=True)
        if solution:
            print('x: {0} \ty: {1}'.format(solution[0][x], solution[0][y]))
        else:
            print('No solution found.')
        expr1_y = sp.solve(expr1, y)[0]
        expr2_y = sp.solve(expr2, y)[0]

        p = sp.plot(expr1_y, expr2_y, legend=True, show=False)
        p[0].line_color = 'b'
        p[1].line_color = 'r'
        p.show()

    try:
        expr1 = input('Enter your first expression in terms of x and y: ')
        expr2 = input('Enter your second expression in terms of x and y: ')

        expr1 = sp.sympify(expr1)
        expr2 = sp.sympify(expr2)
    except SympifyError:
        print('Invalid input.')
    else:
        x, y = sp.symbols('x, y')
        expr1_symbols = expr1.atoms(sp.Symbol)
        expr2_symbols = expr2.atoms(sp.Symbol)

        if len(expr1_symbols) > 2 or len(expr2_symbols) > 2:
            print('The equations must have only two variables - x and y.')
        elif x not in expr1_symbols or y not in expr1_symbols:
            print('First equation must have only x and y variables.')
        elif x not in expr2_symbols or y not in expr2_symbols:
            print('Second equation must have only x and y variables.')
        else:
            sp_plot(expr1, expr2, x, y)
    '''

    # EXC 3
    '''
    def calc_summation(nth_term, n_term):
        n = sp.Symbol('n')
        res = sp.summation(nth_term, (n, 1, n_term))
        sp.pprint(res)

    try:
        nth_term = input('Enter an n-th term: ')
        nth_term = sp.sympify(nth_term)
        n = int(input('Enter number of terms: '))
    except SympifyError:
        print('Invalid input.')
    else:
        calc_summation(nth_term, n)
    '''

    # EXC 4

    '''
    x = sp.Symbol('x')
    ineq_obj = -x**2 + 4 < 0
    lhs = ineq_obj.lhs
    p = sp.Poly(lhs, x)
    rel = ineq_obj.rel_op
    sol = sp.solve_poly_inequality(p, rel)
    print(sol)
    '''

    '''
    x = sp.Symbol('x')
    ineq_obj = ((x-1)/(x+2)) > 0
    lhs = ineq_obj.lhs
    numer, denom = lhs.as_numer_denom()
    p1 = sp.Poly(numer)
    p2 = sp.Poly(denom)
    rel = ineq_obj.rel_op
    sol = sp.solve_rational_inequalities([[((p1, p2), rel)]])
    print(sol)
    '''

    '''
    x = sp.Symbol('x')
    ineq_obj = sp.sin(x) - 0.6 > 0
    sol = sp.solve_univariate_inequality(ineq_obj, x, relational=False)
    print(sol)
    '''

    def isolve(expr, x):
        lhs = expr.lhs
        if lhs.is_polynomial():
            p = sp.Poly(lhs, x)
            rel = expr.rel_op
            sol = sp.solve_poly_inequality(p, rel)
            print(sol)
        elif lhs.is_rational_function():
            numer, denom = lhs.as_numer_denom()
            p1 = sp.Poly(numer)
            p2 = sp.Poly(denom)
            rel = expr.rel_op
            sol = sp.solve_rational_inequalities([[((p1, p2), rel)]])
            print(sol)
        else:
            sol = sp.solve_univariate_inequality(expr, x, relational=False)
            print(sol)

    try:
        expr = sp.sympify(input('Enter your inequality with one term as /x/: '))
    except SympifyError:
        print('Invalid input.')
    else:
        x = sp.Symbol('x')
        param = expr.atoms(sp.Symbol)
        if len(param) > 1 and x not in param:
            print('You have to input expression with one term, /x/: ')
        else:
            print(expr)
            isolve(expr, x)
