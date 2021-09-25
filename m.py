import matplotlib.pyplot as plt
import numpy as np

def f(x, y, x_c, y_c):
    #c = x_c + i y_c
    return x**2 - y**2 + x_c, 2*x*y + y_c

"""
N= 1000
z = np.zeros(shape=(N, 2))
for i in range(N-1):
    x,y = f(z[i][0],z[i][1])
    z[i+1] = np.asarray([x, y])
x = z.T[0]
y = z.T[1]
plt.plot(x, y, '.')
plt.show()
    
"""
def c_in_set(x_c , y_c):
    N= 100
    z = np.zeros(shape=(N+3, 2))
    step = 0
    flag = True
    while (step<N) and flag:
        x,y = f(z[step][0],z[step][1], x_c, y_c)
        z[step+1] = np.asarray([x, y])
        if (not np.isfinite(z[step][0])) or (not np.isfinite(z[step][1])):
            flag = False
        step+=1
    return flag

N = 1000
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
M_set = []
for x_c in x:
    for y_c in y:
        if c_in_set(x_c, y_c):
            M_set.append([x_c, y_c])
M_set = np.asarray(M_set)
M_x = M_set.T[0]
M_y = M_set.T[1]
plt.plot(M_x, M_y, '.')
plt.show()

        
