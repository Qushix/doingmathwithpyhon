import sympy as sp
from fractions import Fraction
import random
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import csv
import math

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

    '''
    taget_score = 20
    def roll():
        return random.randint(1, 6)

    score = 0
    num_rolls = 0
    while score < taget_score:
        num_rolls += 1
        die_roll = roll()
        score += die_roll
        print('Rolled: {0}'.format(die_roll))

    print('Score of {0} achieved after {1} rolls.'.format(score, num_rolls))
    '''

    '''
    def find_prop(score_goal, num_rolls):
        s = sp.FiniteSet(*range(1, 7))
        possibilities = s**num_rolls
        if num_rolls > 1:
            event = []
            for element in possibilities:
                if sum(element) >= score_goal:
                    event.append(element)
        else:
            if num_rolls == 1:
                event = []
                for element in possibilities:
                    if sum(element) >= score_goal:
                        event.append(element)
                    else:
                        event = []

        return event

    score_goal = float(input('Enter score goal that you are willing to achieve: '))
    num_rolls = int(input('Enter maximum number of rolls: '))

    event = find_prop(score_goal, num_rolls)
    event = sp.FiniteSet(*event)
    space = sp.FiniteSet(*range(1, 7)) ** num_rolls
    prop = len(event) / len(space)

    print('Probability of achieving a goal score: {0}.'.format(prop))
    '''

    '''
    def get_index(probability):
        c_probability = 0
        prob_axis = []
        for element in probability:
            c_probability +=element
            prob_axis.append(c_probability)

        r = random.random()
        for index, par in enumerate(prob_axis):
            if r <= par:
                return index
        return len(probability) - 1

    values = [5, 10, 15, 20]
    probability = [1/6, 1/6, 1/3, 1/3]
    ind = get_index(probability)
    print('You achieved: {0}'.format(values[ind]))
    '''

    '''
    def prime_number(value):
        if value != 1:
            space = sp.FiniteSet(*range(2, value))
            for element in space:
                if value % element == 0:
                    return False
        else:
            return False
        return True

    def calc_prime_list(max_value):
        prime_list = []
        for element in range(2, max_value + 1):
            if prime_number(element):
                prime_list.append(element)
            else:
                continue
        return prime_list

    s1 = sp.FiniteSet(*range(1, 20, 2))
    s2 = sp.FiniteSet(*calc_prime_list(20))

    def draw_sets(sets):
        venn2(subsets=sets)
        plt.show()

    draw_sets([s1, s2])
    '''
    # EXC 1
    '''
    def csv_reader(filname):
        football = []
        other = []
        with open(filname) as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                if int(line[1]) == 1:
                    football.append(int(line[0]))
                if int(line[2]) == 1:
                    other.append(int(line[0]))
        return football, other

    def venn(set1, set2):
        set1 = sp.FiniteSet(*set1)
        set2 = sp.FiniteSet(*set2)
        venn2(subsets=(set1, set2), set_labels=('Football', 'Other sports'))
        plt.show()

    football, other = csv_reader('s.csv')
    print(football, other)
    venn(football, other)
    '''
    # EXC 2
    '''
    def calc_mean(dataset):
        return sum(dataset) / len(dataset)

    def calc_expectation(num_rolls):
        results = []
        for num in range(1, num_rolls+1):
            roll = random.randint(1, 6)
            results.append(roll)

        mean_value = calc_mean(results)
        return mean_value

    num_trials = int(input('Enter number of trials: '))
    your_mean = calc_expectation(num_trials)
    print('After {0} your mean is equal to {1}'.format(num_trials, your_mean))
    '''
    # EXC 3
    '''
    def money_game(starting_cash):
        # 1 heads, 2 tails
        pool = starting_cash
        num_toss = 0
        while pool >= 0:
            toss = random.randint(1, 2)
            num_toss += 1
            if toss == 1:
                pool += 1
                print('Heads! Current amount: {0}'.format(pool))
            else:
                pool -= 1.5
                print('Tails! Current amount: {0}'.format(pool))

        return print('Game over :( Current amount: {0}. Coin tosses: {1}'.format(pool, num_toss))

    starting_cash = float(input('Enter your starting amount: '))
    money_game(starting_cash)
    '''
    # EXC 4
    '''
    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

    def initialize_deck():
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                cards.append(card)
        return cards

    def shiffle_and_print(cards):
        random.shuffle(cards)
        for card in cards:
            print('{0} of {1}'.format(card.rank, card.suit))

    cards = initialize_deck()
    shiffle_and_print(cards)
    '''
    # EXC 5

    def circle_points(r, num_points):
        center = (r, r)
        in_circle = 0

        for element in range(num_points):
            x = random.uniform(0, 2 * r)
            y = random.uniform(0, 2 * r)
            d = math.sqrt((x - center[0])**2 + (y-center[1])**2)
            if d <= r:
                in_circle += 1

        area_of_sq = (2*r)**2
        area_est = area_of_sq * (in_circle/num_points)
        pi_est = 4 * (in_circle/num_points)
        return area_est, pi_est

    num_points = int(input('Enter number of points: '))
    r = float(input('Enter radius of circle: '))

    print('Area o circle: {0} \tEstimated one for {1} points: {2} \t Estimated pi: {3}'
          .format(math.pi*r**2, num_points, circle_points(r, num_points)[0], circle_points(r, num_points)[1]))










