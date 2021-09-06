import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

beta = .9

#time series set
#you can change it to your own dataset
y = np.random.normal(0, 10, size=(1000,1))
t = np.arange(len(y))

b = [0]
# the case of the first iteration (i==0) is taken by that for
#bias correction reasons
for i in range(len(y)):
    if i==0:
        b.append((beta * b[i] + (1 - beta) * y[i]) / (1 - beta**(i+1)))
    else:
        b.append(beta * b[i] + (1 - beta) * y[i])
b = np.array(b[1:])

plt.plot(t, y)
plt.plot(t, b)
plt.show()
