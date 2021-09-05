import numpy as np
from matplotlib import pyplot as plt

epsilon = 10**(-7)
N =10**(4)

def f(x):
    return x**2

t = np.linspace(.5 ,10,N)
y = f(t)
#divide with 2 * epsilon for O(epsilon^2) error
#divide with epsilon for O(epsilon) error
der = (f(t + epsilon) - f(t - epsilon)) / (2 * epsilon)

plt.figure()
plt.axes()
plt.plot(t, y, 'b')
plt.plot(t, der, 'r')
plt.legend(['f(x)', 'f\' (x)'])
plt.show()
