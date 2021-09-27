import matplotlib.pyplot as plot
import numpy


def main():
    x = numpy.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
    y = numpy.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100])
    reg = numpy.polyfit(x, y, 3)
    polynomial = numpy.poly1d(reg)
    regression = [polynomial(i) for i in x]

    plot.figure(1)
    plot.scatter(x, y, label='data')
    plot.plot(x, regression, color='red', label='regression curve')
    plot.legend()
    plot.title('Data regression fit')

    plot.show()


main()
