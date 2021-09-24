import numpy as np
import matplotlib.pyplot as plt

def f1(t, x):
    sigma = 10
    return sigma * (x[1] - x[0])

def f2(t, x):
    ar = 28
    return x[0] * (ar - x[2]) - x[1]

def f3(t, x):
    beta = 8/3
    return x[0] * x[1] - beta * x[2]

def euler(a, b, n, x_0):
    h = (b-a) / n
    t = np.linspace(a, b, n)
    y = np.zeros(shape=(n, 3))
    y[0][0], y[0][1], y[0][2] = x_0[0], x_0[1], x_0[2]
    print(y)
    for i in range(n-1):
        y[i+1] = y[i] + h * np.asarray([f1(t[i], y[i]),
                                                          f2(t[i], y[i]),
                                                         f3(t[i], y[i])])
    return y
def _3d_plot(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z)
    plt.show()

N = 10000
x_0 = np.asarray([2, 3, 6])
yy = euler(0, 100, N, x_0)
t = np.linspace(0, 10, N)
x = yy.T[0]
y = yy.T[1]
z = yy.T[2]

_3d_plot(x, y, z)
