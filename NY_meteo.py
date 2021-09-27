import matplotlib.pyplot as plot
import numpy


def ny_1():
    days = [i for i in range(1, 31)]
    temperature = [8.3, 1.8, 6, 12, 14.1, 14, 14.5, 14.2, 10.5, 13.5, 11.2, 8.5, 11.7, 15.5, 10.8, 8.3, 9.5, 12.9, 14.8,
                   17.2, 12.4, 6, 11.9, 16.2, 12.7, 11.1, 12.5, 16.8, 19, 17.1]
    rain = [9.65, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10.16, 13.97, 0, 0, 23.62, 0.76, 0, 0, 0, 0, 6.86, 0, 0, 10.41, 2.29,
            0, 0, 0.76, 0]

    rainy_days = 0
    sunny_days = 0
    little_rain = 0
    for i in range(30):
        if rain[i] == 0:
            sunny_days += 1
        elif rain[i] < 7:
            little_rain += 1
        else:
            rainy_days += 1

    plot.figure(1)
    plot.plot(temperature, label='temperature')
    plot.bar(days, rain, color='r', label='rain')
    plot.legend()
    plot.title('Weather in NY')

    plot.figure(2)
    labels = 'Rainy Days', 'Sunny Days', 'Little Rain'
    amounts = [rainy_days, sunny_days, little_rain]
    plot.pie(amounts, labels=labels, autopct='%.1f%%')

    plot.show()


def ny_2():
    days = numpy.array([i for i in range(1, 31)])
    temperature = numpy.array([8.3, 1.8, 6, 12, 14.1, 14, 14.5, 14.2, 10.5, 13.5, 11.2, 8.5, 11.7, 15.5, 10.8, 8.3, 9.5,
                               12.9, 14.8, 17.2, 12.4, 6, 11.9, 16.2, 12.7, 11.1, 12.5, 16.8, 19, 17.1])
    reg = numpy.polyfit(days, temperature, 1)
    polynomial = numpy.poly1d(reg)
    regression = [polynomial(i) for i in days]
    plot.plot(temperature, label='temperature')
    plot.plot(regression, color='r', label='trend')
    plot.legend()
    plot.title('Temperature in NY')
    plot.show()


ny_1()
ny_2()
