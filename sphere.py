import math


def volume(radius):
    return (4/3)*math.pi*(radius**3)


def area(radius):
    return 4*math.pi*(radius**2)


def main():
    radius = float(input('give me a radius: '))
    precision = int(input('give me a cutoff: '))
    print('volume is ' + str(round(volume(radius), precision)))
    print('area is ' + str(round(area(radius), precision)))


main()
