import matplotlib.pyplot as plt
if __name__ == "__main__":
    '''
    x = [1, 2, 3]
    y = [2, 4, 6]
    plt.plot(x, y, marker='o')
    plt.show()
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
    plt.savefig('xd.pdf')
    plt.show()