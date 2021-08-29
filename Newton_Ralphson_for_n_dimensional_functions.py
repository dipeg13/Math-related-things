import matplotlib.pyplot as plt
import numpy as np
import math

#It seems that Newton_Raplphson method is unstable for multivariate functions
#that seem to be not trivial
def f(x):
    #x generally is an n-tuple
    #here f=f(x,y)=x^2+y^2 is a paraboloid
    return (x[0] -1)**2 + (x[1] +3)**2

def gradient_f(x):
    #x generally is an n-tuple
    #here f=f(x,y)=x^2+y^2, so grad(f(x))=(2x, 2y)
    return np.asarray([2 * (x[0] - 1), 2 * (x[1] + 3)])
#-----------------------------------------------------
#In this section we must create the derivatives used to comput the Hessian matrix at each point needed
#-----------------------------------------------------
def d2f_dx1dx2(x):
    return 0

def d2f_d2x1(x):
    return 2

def d2f_d2x2(x):
    return 2

def Hessian_f(x):
    H_f = np.zeros((2,2))
    H_f[0][0] = d2f_d2x1(x)
    H_f[0][1] = d2f_dx1dx2(x)
    H_f[1][0] = d2f_dx1dx2(x)
    H_f[1][1] = d2f_d2x2(x)
    return H_f
"""
def f(x):
    #x generally is an n-tuple
    #here f=f(x,y)=x^2+y^2 is a paraboloid
    return math.exp(-1/3 * x[0]**3 + x[0] - x[1]**2)

def gradient_f(x):
    #x generally is an n-tuple
    #here f=f(x,y)=x^2+y^2, so grad(f(x))=(2x, 2y)
    return np.asarray([ (-x[0]**2 +1) * f(x), -2 * x[1] * f(x)])
#-----------------------------------------------------
#In this section we must create the derivatives used to comput the Hessian matrix at each point needed
#-----------------------------------------------------
def d2f_dx1dx2(x):
    return -2 * x[1] * (1-x[0]**2) * f(x)

def d2f_d2x1(x):
    return (-2 * x[0] + ( 1 - x[0]**2)**2) * f(x)

def d2f_d2x2(x):
    return (-2 + 4 * x[1]**2) * f(x)
#-----------------------------------------------------
#Definition of derivatives ended
#-----------------------------------------------------

#-----------------------------------------------------
#In this section we must define th Hessian matrix
#-----------------------------------------------------
def Hessian_f(x):
    H_f = np.zeros((2,2))
    H_f[0][0] = d2f_d2x1(x)
    H_f[0][1] = d2f_dx1dx2(x)
    H_f[1][0] = d2f_dx1dx2(x)
    H_f[1][1] = d2f_d2x2(x)
    return H_f
#-----------------------------------------------------
#End of Hessian definition
#-----------------------------------------------------
"""
def NR_nD(x_0, tolerance):
    while np.linalg.norm(gradient_f(x_0)) > tolerance:
        x_0 = x_0 - np.dot(np.linalg.inv(Hessian_f(x_0)),gradient_f(x_0))
    return x_0

N=10000
tx = np.linspace(0, 2, N)
ty = np.linspace(-.5, .5, N)
#At N**2 below, we have 2, because of the dimension of the space
#For example, for R^14, except the extended parametrization about the gradients above
#we should also have N**14 point
points = np.empty((N**2))

f_min = NR_nD([0,0], 10**(-3))


        
