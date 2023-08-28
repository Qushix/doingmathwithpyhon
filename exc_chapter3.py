from collections import Counter
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

    '''
    def median(data_set):
        N = len(data_set)
        data_set.sort()
        if N % 2 == 0:
            return (data_set[int(N/2) - 1] + data_set[int(N/2)]) / 2
        else:
            return data_set[int((N+1)/2)]


    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 900]
    median_donation = median(donations)
    N = len(donations)
    print('Median donation over the last {0} days is {1}'.format(N, median_donation))
    '''

    '''
    def mode(data_set):
        set = Counter(data_set)
        max_times = set.most_common(1)[0][1]

        modes = []
        for element in set.most_common():
            if element[1] == max_times:
                modes.append(element[0])
        return modes

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


    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = calc_variance(donations)
    print('Variance: {0} \tStandard deviation: {1}'.format(variance, variance**0.5))
    '''

    def find_corr(x, y):
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
