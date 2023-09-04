import random
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import matplotlib.cm as cm

if __name__ == '__main__':
    '''
    x = [1, 2, 3]
    y = [1, 2, 3]
    fig = plt.figure()
    axes = plt.axes()
    plt.plot(x, y)
    plt.show()
    '''

    '''
    def create_circle():
        r = 0.5
        circle = plt.Circle((0, 0), r, fc='g', ec='r')
        return circle


    def show_shape(patch):
        ax = plt.gca()
        ax.add_patch(patch)
        ax.set_aspect('equal')
        plt.axis('scaled')
        plt.show()

    c = create_circle()
    show_shape(c)
    '''

    '''
    def create_circle():
        r = 0.05
        circle = plt.Circle((0, 0), r)
        return circle

    def update_radius(i, circle):
        circle.radius = i*0.5
        return circle,

    def circle_animation():
        fig = plt.gcf()
        ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
        ax.set_aspect('equal')
        circle = create_circle()
        ax.add_patch(circle)
        anim = animation.FuncAnimation(
            fig, update_radius, fargs=(circle,), frames=30, interval=10
        )
        plt.title('Simple Circle Animation')
        plt.show()

    circle_animation()
    '''

    '''
    g = 9.81

    def create_intervals(u, theta):
        start = 0
        intervals = []
        interval = 0.005
        t_max = 2*u*math.sin(theta)/g
        while start < t_max:
            intervals.append(start)
            start += interval
        return intervals

    def update_position(i, circle, intervals, u, theta):
        t = intervals[i]
        x = u*math.cos(theta)*t
        y = u*math.sin(theta)*t - 0.5*g*t*t
        circle.center = x, y
        return circle,

    def create_animation(u, theta):
        intervals = create_intervals(u, theta)

        fig = plt.gcf()

        tmax = u*math.sin(theta)/g
        xmin = 0
        xmax = u*math.cos(theta)*intervals[-1]
        ymin = 0
        ymax = u*math.sin(theta)*tmax - 0.5*g*tmax**2
        ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, 1.2*ymax))
        ax.set_aspect('equal')
        circle = plt.Circle((xmin, ymin), 1)
        ax.add_patch(circle)

        anim = animation.FuncAnimation(
            fig, update_position, fargs=(circle, intervals, u, theta), frames=len(intervals), interval=10, repeat=False
        )

        plt.title('Projectile motion')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the initial angle of projection (degrees): '))
    except ValueError:
        print('Enter valid input.')
    else:
        theta = math.radians(theta)
        create_animation(u, theta)
    '''

    '''
    def transformation_1(p):
        x = p[0]
        y = p[1]
        return x + 1, y - 1

    def transformation_2(p):
        x = p[0]
        y = p[1]
        return x + 1, y + 1

    def transform(p):
        transformations = [transformation_1, transformation_2]
        t = random.choice(transformations)
        x, y = t(p)
        return x, y

    def create_trajectory(p, n):
        x = [p[0]]
        y = [p[1]]
        for i in range(n):
            p = transform(p)
            x.append(p[0])
            y.append(p[1])
        return x, y

    p = (1, 1)
    n = int(input('Enter a number of iterations: '))
    x, y = create_trajectory(p, n)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    '''

    '''
    def transformation1(p):
        x = p[0]
        y = p[1]
        x1 = 0.85*x + 0.04*y
        y1 = -0.04*x + 0.85*y + 1.6
        return x1, y1

    def transformation2(p):
        x = p[0]
        y = p[1]
        x1 = 0.2*x - 0.26*y
        y1 = 0.23*x + 0.22*y + 1.6
        return x1, y1

    def transformation3(p):
        x = p[0]
        y = p[1]
        x1 = -0.15*x + 0.28*y
        y1 = 0.26*x + 0.24*y + 0.44
        return x1, y1

    def transformation4(p):
        x = p[0]
        y = p[1]
        x1 = 0
        y1 = 0.16*y
        return x1, y1

    def get_index(probability):
        r = random.random()
        c_probability = 0
        sum_probability = []
        for p in probability:
            c_probability += p
            sum_probability.append(c_probability)
        for index, sp in enumerate(sum_probability):
            if r <= sp:
                return index
        return len(probability) - 1

    def transform(p):
        transformations = [transformation1, transformation2, transformation3, transformation4]
        probability = [0.85, 0.07, 0.07, 0.01]
        tindex = get_index(probability)
        t = transformations[tindex]
        x, y = t(p)
        return x, y

    def draw_fern(n):
        x = [0]
        y = [0]

        x1, y1 = 0, 0
        for i in range(n):
            x1, y1 = transform((x1, y1))
            x.append(x1)
            y.append(y1)

        return x, y

    n = int(input('Enter the number of points in Fern: '))
    x, y = draw_fern(n)
    plt.plot(x, y, 'o', markersize=1)
    plt.title('Fern with {0} points'.format(n))
    plt.show()
    '''
    # EXC 1
    '''
    def draw_square():
        square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed=True)
        return square

    def draw_circle(x, y):
        circle = plt.Circle((x, y), 0.5, fc='y')
        return circle

    def draw_all():
        ax = plt.gca()
        square = draw_square()
        ax.add_patch(square)
        y = 1.5
        while y < 5:
            x = 1.5
            while x < 5:
                circle = draw_circle(x, y)
                ax.add_patch(circle)
                x += 1
            y += 1
        plt.axis('scaled')
        plt.show()

    draw_all()
    '''
    # EXC 2
    '''
    def transformation1(p):
        x = p[0]
        y = p[1]
        x1 = 0.5*x
        y1 = 0.5*y
        return x1, y1

    def transformation2(p):
        x = p[0]
        y = p[1]
        x1 = 0.5*x + 0.5
        y1 = 0.5*y + 0.5
        return x1, y1

    def transformation3(p):
        x = p[0]
        y = p[1]
        x1 = 0.5*x + 1
        y1 = 0.5*y
        return x1, y1

    def transform(p):
        transformations = [transformation1, transformation2, transformation3]
        t = random.choice(transformations)
        x, y = t(p)
        return x, y

    def draw_triangle(n):
        x1 = 0
        y1 = 0

        x = [0]
        y = [0]
        for i in range(n):
            x1, y1 = transform((x1, y1))
            x.append(x1)
            y.append(y1)

        plt.plot(x, y, 'o', markersize=1)
        plt.title('Sierpiński triangle made of {0} points'.format(n))
        plt.show()

    n = int(input('Enter a number of points: '))
    draw_triangle(n)
    '''
    # EXC 3
    '''
    def transformation(p):
        x = p[0]
        y = p[1]
        x1 = y + 1 - 1.4*x**2
        y1 = 0.3*x
        return x1, y1

    def update_points(i, x, y, curve):
        curve.set_data(x[:i], y[:i])
        return curve
    def draw_henon(n):
        x = [0]
        y = [0]

        x1 = 0
        y1 = 0
        for i in range(n):
            x1, y1 = transformation((x1, y1))
            x.append(x1)
            y.append(y1)

        fig = plt.gcf()
        ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(y), max(y)))
        plot = plt.plot([], [], 'o', markersize=1)[0]
        anim = animation.FuncAnimation(fig, update_points, fargs=(x, y, plot), frames=len(x), interval=25)
        plt.title('Hénon function made of {0} points'.format(n))
        plt.show()

    n = int(input('Enter number of points: '))
    draw_henon(n)
    '''
    # EXC 4

    x0, x1 = -2.5, 1
    y0, y1 = -1, 1

    def initialize_image(x_p, y_p):
        image = []
        for y in range(y_p):
            x_list = []
            for x in range(x_p):
                x_list.append(0)
            image.append(x_list)
        return image

    def color_points():
        x_p = 300
        y_p = 300
        max_iteration = 1000
        image = initialize_image(x_p, y_p)
        dx = (x1 - x0) / (x_p-1)
        dy = (y1 - y0) / (y_p-1)
        x_coords = [x0 + i*dx for i in range(x_p)]
        y_coords = [y0 + i*dy for i in range(y_p)]

        for i, x in enumerate(x_coords):
            for k, y in enumerate(y_coords):
                z1 = complex(0, 0)
                iteration = 0
                c = complex(x, y)
                while abs(z1) < 2 and iteration < max_iteration:
                    z1 = z1**2 + c
                    iteration += 1
                image[k][i] = iteration
        return image

    image = color_points()
    plt.imshow(image, origin='lower', extent=(x0, x1, y0, y1), cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()








