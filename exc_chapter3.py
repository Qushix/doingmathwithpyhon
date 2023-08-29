from collections import Counter
import matplotlib.pyplot as plt
import csv
import math
if __name__ == '__main__':
    '''
    def mean(data_set):
        s = sum(data_set)
        N = len(data_set)
        return s/N

    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean_donation = mean(donations)
    N = len(donations)
    print('Mean donation over the last {0} days is {1}'.format(N, mean_donation))
    '''
    def median(data_set):
        N = len(data_set)
        data_set.sort()
        if N % 2 == 0:
            return (data_set[int(N/2) - 1] + data_set[int(N/2)]) / 2
        else:
            return data_set[int((N+1)/2)]

    '''
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 900]
    median_donation = median(donations)
    N = len(donations)
    print('Median donation over the last {0} days is {1}'.format(N, median_donation))
    '''

    def mode(data_set):
        set = Counter(data_set)
        max_times = set.most_common(1)[0][1]

        modes = []
        for element in set.most_common():
            if element[1] == max_times:
                modes.append(element[0])
        return modes

    '''
    scores = [5, 5, 5, 4, 4, 4, 9, 1, 3]
    mode_scores = mode(scores)
    N = len(scores)
    print('Mode score out of {0} students is {1}'.format(N, mode_scores))
    '''

    '''
    def frequency_table(data_set):
        pairs = Counter(data_set)
        table_freq = pairs.most_common()
        table_freq.sort()
        print('Number\tFrequency')
        for element in table_freq:
            print('{0}\t\t\t{1}'.format(element[0], element[1]))

    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)
    '''

    '''
    def range(data_set):
        range_val = max(data_set) - min(data_set)
        return max(data_set), min(data_set), range_val


    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    highest, lowest, r = range(donations)
    print('Highest {0}, Lowest {1}, Range {2}'.format(highest, lowest, r))
    '''

    def calc_mean(data_set):
        mean = sum(data_set) / len(data_set)
        return mean

    def find_differences(data_set):
        mean = calc_mean(data_set)
        diff = []
        for element in data_set:
            diff.append(mean - element)
        return diff

    def calc_variance(data_set):
        diff = find_differences(data_set)
        diff_sq = []
        for element in diff:
            diff_sq.append(element**2)
        variance = sum(diff_sq) / len(data_set)

        return variance

    '''
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calc_variance(donations)
    print('Variance: {0} \tStandard deviation: {1}'.format(variance, variance**0.5)) 
    '''
    def find_corr(x, y):
        if len(x) == len(y):
            prod = []
            for xi, yi in zip(x, y):
                prod.append(xi*yi)

            sum_prod = sum(prod)

            sum_x = sum(x)
            sum_y = sum(y)
            sum_x_sq = sum_x**2
            sum_y_sq = sum_y**2

            x_square = []
            for xi in x:
                x_square.append(xi**2)
            x_square_sum = sum(x_square)

            y_square = []
            for yi in y:
                y_square.append(yi ** 2)
            y_square_sum = sum(y_square)

            n = len(x)

            numerator = n*sum_prod - sum_x*sum_y
            denominator1 = n*x_square_sum - sum_x_sq
            denominator2 = n*y_square_sum - sum_y_sq
            denominator = (denominator1*denominator2)**0.5
            correlation = numerator/denominator

            return correlation
        else:
            print('X and Y should have equal number of elements.')
            return None
    '''
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    plt.scatter(x, y)
    plt.show()
    '''

    '''
    def sum_data(filename):
        s = 0
        with open(filename) as f:
            for line in f:
                s = s + float(line)
        print('Sum of the numbers: {0}'.format(s))

    sum_data('D:\Python Ebook\doingmathwithpython\my_Data.txt')
    '''

    '''
    def list_creator(filename):
        my_list = []
        with open(filename) as f:
            for line in f:
                my_list.append(float(line))
        return my_list

    generated_list = list_creator('my_Data.txt')
    print(sum(generated_list))
    '''

    '''
    def scatter_plot(x, y):
        plt.scatter(x, y)
        plt.show()
    '''

    '''
    def read_csv(filename):

        numbers = []
        squared = []
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                numbers.append(int(row[0]))
                squared.append(int(row[1]))
            return numbers, squared

    numbers, squared = read_csv('my_CSV.csv')
    scatter_plot(numbers, squared)
    '''

    '''
    def read_csv(filename):
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)

            summer = []
            highest_correlated = []
            for row in reader:
                summer.append(float(row[1]))
                highest_correlated.append(float(row[2]))

        return summer, highest_correlated

    summer, highest_correlated = read_csv('correlate-summer.csv')
    corr = find_corr(summer, highest_correlated)
    print('Highest correlation: {0}'.format(corr))
    scatter_plot(summer, highest_correlated)
    '''

    # EXC 1

    '''
    x = [1, 2, 3]
    y = [1, 4, 9]

    corr = find_corr(x, y)
    if not corr:
        print('Correlation correlation could not be calculated')
    else:
        print('The correlation coefficient between x and y is {0}'.format(corr))
    '''

    # EXC 2
    '''
    def read_txt(filename):
        new_list = []
        with open(filename) as f:
            for line in f:
                new_list.append(int(line))
        return new_list

    gen_list = read_txt('my_Data.txt')
    mean = calc_mean(gen_list)
    median = median(gen_list)
    mode = mode(gen_list)
    variance = calc_variance(gen_list)
    st_dev = variance**0.5

    print('Mean: {0}, Median: {1}, Mode: {2}, Variance: {3}, Standard deviation: {4}'.format(mean, median, mode, variance, st_dev))
    '''

    # EXC 3
    '''
    def csv_reader(filename):
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)

            population_US = []
            years = []
            for row in reader:
                years.append(row[0].split('-')[0])
                population_US.append(float(row[1]))
            years.reverse()
            population_US.reverse()
        return years, population_US

    def plot_population(population, years):
        plt.figure(1)
        xaxis_positions = range(0, len(years))
        plt.plot(population, 'r-')
        plt.title('Total population in US')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.xticks(xaxis_positions, years, rotation=45)

    def plot_population_diff(growth, years):
        xaxis_positions = range(0, len(years)-1)
        xaxis_labels = ['{0}-{1}'.format(years[i], years[i+1]) for i in range(len(years)-1)]
        plt.figure(2)
        plt.plot(growth, 'r-')
        plt.title('Population Growth in consecutive years')
        plt.ylabel('Population Growth')
        plt.xticks(xaxis_positions, xaxis_labels, rotation=45)

    def calc_growth(population):
        growth = []
        for i in range(0, len(population)-1):
            diff = population[i+1] - population[i]
            growth.append(diff)
        return growth

    years, population_US = csv_reader('USA_SP_POP_TOTL.csv')

    mean = calc_mean(population_US)
    median = median(population_US)
    mode = mode(population_US)
    variance = calc_variance(population_US)
    st_dev = variance ** 0.5

    print('Mean: {0}, Median: {1}, Variance: {2}, Standard deviation: {3}'.format(mean, median, variance, st_dev))

    plot_population(population_US, years)
    growth = calc_growth(population_US)
    plot_population_diff(growth, years)
    plt.show()
    '''

    # EXC 4
    '''
    def read_txt(filename):
        with open(filename) as f:
            new_list = []
            for line in f:
                new_list.append(float(line))
        return new_list

    def give_percentile(dataset, percentile):
        dataset = sorted(dataset)
        n = len(dataset)
        i = n * (percentile/100) + 0.5
        if i.is_integer():
            return dataset[i-1]
        elif percentile == 0:
            return dataset[0]
        elif percentile == 100:
            return dataset[-1]
        elif percentile < 0 or percentile > 100:
            return None
        else:
            k = int(math.floor(i))
            f = i - k
            return (1-f)*dataset[k-1] + f*dataset[k]

    dataset = read_txt('my_Data.txt')
    p = float(input('Enter specific percentile: '))
    percentile = give_percentile(dataset, p)
    if not percentile:
        print('You entered wrong percentile.')
    else:
        print('Achieved percentile: {0}'.format(percentile))
    '''

    # EXC 5

    '''
    def create_classs(numbers, n):
        low = min(numbers)
        high = max(numbers)
        width = (high - low)/n
        classes = []
        a = low
        b = low + width

        while a < (high-width):
            classes.append((a, b))
            a = b
            b = a + width
        classes.append((a, high+1))
        return classes

    def read_txt(filename):
        with open(filename) as f:
            new_list = []
            for line in f:
                new_list.append(float(line))
        return new_list

    def classify(numbers, classes):
        count = [0]*len(classes)
        for n in numbers:
            for index, c in enumerate(classes):
                if n >= c[0] and n < c[1]:
                    count[index] += 1
                    break
        return count

    num_classes = int(input('Enter the number of classes: '))
    numbers = read_txt('my_Data.txt')
    classes = create_classs(numbers, num_classes)
    count = classify(numbers, classes)
    for c, cnt in zip(classes, count):
        print('{0:.2f} - {1:.2f} \t {2}'.format(c[0], c[1], cnt))
    '''