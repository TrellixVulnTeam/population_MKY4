# import pylab
# import matplotlib.pyplot as plt
import math
from save import *


def make_data(x, y, alpha, delta):
    h = 0.01
    xlist = []
    ylist = []
    for i in range(10000):
        km1 = h * f(x, y, alpha)
        lm1 = h * g(x, y, alpha, delta)
        km2 = h * f(x + km1/2, y + lm1/2, alpha)
        lm2 = h * g(x + km1/2, y + lm1/2, alpha, delta)
        km3 = h * f(x + km2/2, y + lm2/2, alpha)
        lm3 = h * g(x + km2/2, y + lm2/2, alpha, delta)
        km4 = h * f(x + km3, y + lm3, alpha)
        lm4 = h * g(x + km3, y + lm3, alpha, delta)
        x1 = x + (km1 + 2 * km2 + 2 * km3 + km4)/6
        y1 = y + (lm1 + 2 * lm2 + 2 * lm3 + lm4)/6
        if math.fabs(x1 - x) < 0.00001 and math.fabs(y1 - y) < 0.00001:
            return xlist, ylist
        xlist.append(x1)
        ylist.append(y1)
        x = x1
        y = y1
    return xlist, ylist


def f(x, y, alpha):
    return x - (x*y)/(1+alpha*x) - 0.01*x*x


def g(x, y, alpha, delta):
    return -1*y + (x*y)/(1 + alpha*x)-delta*y*y


def make_data1(x, y, alpha, delta, h):
    xlist = []
    ylist = []
    for i in range(10000):
        km1 = h*f(x, y, alpha)
        lm1 = h*g(x, y, alpha, delta)
        km2 = h*f(x + km1/2, y + lm1/2, alpha)
        lm2 = h*g(x + km1/2, y + lm1/2, alpha, delta)
        km3 = h*f(x + km2/2, y + lm2/2, alpha)
        lm3 = h*g(x + km2/2, y + lm2/2, alpha, delta)
        km4 = h*f(x + km3, y + lm3, alpha)
        lm4 = h*g(x + km3, y + lm3, alpha, delta)
        x1 = x + (km1 + 2*km2 + 2*km3 + km4)/6
        y1 = y + (lm1 + 2*lm2 + 2*lm3 + lm4)/6
        if x1 > 100 or y1 > 20:
            return xlist, ylist
        xlist.append(x1)
        ylist.append(y1)
        x = x1
        y = y1
    return xlist, ylist

def main(alpha, delta):
    x, y = make_data(20, 16, alpha, delta)
    x1, y1 = make_data(21.5, 15, alpha, delta)
    x2, y2 = make_data(60, 15, alpha, delta)
    x3, y3 = make_data(100, 16, alpha, delta)
    x4, y4 = make_data(90, 2, alpha, delta)
    x5, y5 = make_data(2.1, 0.1, alpha, delta)
    matlab_export(x, y, "tr.txt")
    matlab_export(x1, y1, "tr1.txt")
    matlab_export(x2, y2, "tr2.txt")
    matlab_export(x3, y3, "tr3.txt")
    matlab_export(x4, y4, "tr4.txt")
    matlab_export(x5, y5, "tr5.txt")
    # x3, y3 = make_data(20, 16, alpha, delta)
    # x4, y4 = make_data(47, 23, alpha, delta)
    # x5, y5 = make_data(2.1, 0.1, alpha, delta)

    # x6, y6 = make_data(50, 23, alpha, delta)
    sep1, sep2 = make_data1(0, 0.00001, alpha, delta, -0.01)
    matlab_export(sep1, sep2, "sep.txt")
    # plt.plot(x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)
    # plt.plot(sep1, sep2, 'r:')
    # plt.xlabel(r'$X$')
    # plt.ylabel(r'$Y$')
    # plt.title(r'$Область 7$')
    # plt.axis([0, 120, 0, 12])
    # plt.grid(True)
    # pylab.show()


if __name__ == "__main__":
    main(0.4, 0.1)
