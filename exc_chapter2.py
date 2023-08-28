import matplotlib.pyplot as plt
import math
if __name__ == "__main__":
    '''
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y, marker='o')
    plt.show()
    '''
    '''
    nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
    nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
    nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

    months = range(1, 13)

    plt.plot(months, nyc_temp_2000)
    plt.plot(months, nyc_temp_2006)
    plt.plot(months, nyc_temp_2012)
    plt.legend([2000, 2006, 2012], loc='upper left')
    plt.title('Monthly average temperatures at NYC')
    plt.xlabel('Month')
    plt.ylabel('Temp. [F]')
    plt.savefig('xd.jpg')
    plt.show()
    '''

    '''
    def grav_F():
        m_1 = 0.5
        m_2 = 1.5
        G = 6.674e-11
        r = range(100, 1001, 50)
        F = []

        for dist in r:
            F_el = (G * m_1 * m_2) / dist**2
            F.append(F_el)

        plt.plot(r, F)
        plt.show()

    grav_F()
    '''
    '''
    def plot_ball(x, y):
        plt.plot(x, y)
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')
        plt.title('Projectile motion of a ball')

    def frange(start, final, spaces):
        numbers = []
        while start < final:
            numbers.append(start)
            start = start + spaces
        return numbers
    def ball(u, theta):
        theta = math.radians(theta)
        g = 9.8
        t_flight = (2 * u * math.sin(theta)) / g
        t = frange(0, t_flight, 0.001)

        x = []
        y = []
        for t_el in t:
            x.append(u * math.cos(theta) * t_el)
            y.append(u * math.sin(theta) * t_el - 0.5 * g * t_el**2)

        plot_ball(x, y)
    '''
    '''
    try:
        u = float(input('Enter starting velocity (m/s): '))
        theta = float(input('Enter starting angle (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        ball(u, theta)
        plt.show()
    '''
    '''
    u_list = [20, 40, 60]
    for u in u_list:
        ball(u, 45)
    plt.legend(['20', '40', '60'])
    plt.show()
    '''

    # EXC1
    '''
    time = ['11 AM', '0 PM', '1 PM']
    temp = [23, 24, 25]
    # x = range(1, len(time) + 1)

    plt.plot(time, temp, 'o')
    plt.xticks(time, ['j', 'k', 'l'])
    plt.xlabel('Time of a day')
    plt.ylabel('Temperature [degC]')
    plt.grid()
    # plt.xlim([1, 3])
    plt.ylim([20, 30])
    plt.show()
    '''

    # EXC2
    '''
    x_values = range(-1, 9, 1)
    y_values = []
    for x in x_values:
        y = x**2 + 2*x + 1
        y_values.append(y)
        print('x={0} y={1}'.format(x, y))

    plt.plot(x_values, y_values)
    plt.xlim([x_values[0], x_values[-1]])
    plt.ylim([y_values[0], y_values[-1]])
    plt.grid(which='major')
    plt.show()
    '''
    # EXC3
    '''
    def plot_ball(x, y):
        plt.plot(x, y)
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')
        plt.title('Projectile motion of a ball')

    def frange(start, final, spaces):
        numbers = []
        while start < final:
            numbers.append(start)
            start = start + spaces
        return numbers

    def ball(u, theta):
        theta = math.radians(theta)
        g = 9.8
        t_flight = (2 * u * math.sin(theta)) / g
        print('Time of the flight: {0}'.format(t_flight))
        t = frange(0, t_flight, 0.001)

        x = []
        y = []
        for t_el in t:
            x.append(u * math.cos(theta) * t_el)
            y.append(u * math.sin(theta) * t_el - 0.5 * g * t_el ** 2)

        x_max = max(x)
        y_max = max(y)
        print('Maximum horizontal distance: {0}'.format(x_max))
        print('Maximum vertical distance: {0}'.format(y_max))
        plot_ball(x, y)

    try:
        times = int(input('How many trajectories? '))
        u_list = []
        theta_list = []
        for element in range(times):
            u = float(input('Enter starting velocity {0} (m/s): '.format(element+1)))
            theta = float(input('Enter starting angle {0} (degrees): '.format(element+1)))
            u_list.append(u)
            theta_list.append(theta)
    except ValueError:
        print('You entered an invalid input')
    else:
        for element in range(times):
            ball(u_list[element], theta_list[element])
        legend = []
        for element in range(times):
            legend.append('{0} - {1}'.format(u_list[element], theta_list[element]))
        plt.legend(legend)
        plt.show()
    '''
    # EXC4
    '''
    def bar_chart(data, labels):
        num_bars = len(data)
        positions = range(1, num_bars + 1)
        plt.barh(positions, data, align='center')
        plt.yticks(positions, labels)
        plt.xlabel('Expanditures')
        plt.ylabel('Type')
        plt.grid()

    num_cat = int(input('Enter a number of categories: '))
    type_cat_list = []
    expenditure_list = []
    for i in range(num_cat):
        type_cat = input('Enter category {0}: '.format(i + 1))
        type_cat_list.append(type_cat)
        expenditure = float(input('Expenditure {0}: '.format(i + 1)))
        expenditure_list.append(expenditure)

    bar_chart(expenditure_list, type_cat_list)
    plt.show()
    '''

    # EXC 5
    def fibo(n):
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        # n > 2
        a = 1
        b = 1
        # First two members of the series
        series = [a, b]
        for i in range(n):
            c = a + b
            series.append(c)
            a = b
            b = c
        return series

    def plot_ratio(series):
        ratios = []
        for i in range(len(series) - 1):
            ratios.append(series[i+1]/series[i])
        plt.plot(ratios)
        plt.show()

    num = 100
    series = fibo(num)
    plot_ratio(series)
