from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
from Linear_Interpolution import plot

def builtin(x,y):
    f = CubicSpline(x, y, bc_type='natural')
    x_new = np.linspace(0, 2, 80)
    y_new = f(x_new)
    print("xnew ",x_new," y_new ",y_new)
    plt.figure(figsize = (10,8))
    plt.plot(x_new, y_new, 'b')
    plt.plot(x, y, 'bo')
    plt.title('Quadratic Interpolation Builtin')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def ploting(x,y,title):
    plt.figure(figsize = (10,8))
    plt.plot(x,y,'b')
    plt.plot(x, y, 'ro')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

x = [0, 8, 20]
y = [1, 3, 2]
# builtin(x,y)

def Qd_inter(x,y,n,X):
    # # Reading number of unknowns
    # n = int(input('Enter number of data points: '))

    # # Making numpy array of n & n x n size and initializing 
    # # to zero for storing x and y value along with differences of y
    # x = np.zeros((n))
    # y = np.zeros((n))


    # # Reading data points
    # print('Enter data for x and y: ')
    # for i in range(n):
    #     x[i] = float(input( 'x['+str(i)+']='))
    #     y[i] = float(input( 'y['+str(i)+']='))
    # xp = float(input('Enter interpolation point: '))
    xp=float(X)
    yp = 0
    res=[]
    for i in range(n):        
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]    
        res.append(yp)
    print('Quadratic Interpolated value at %.3f is %.3f.' % (xp, yp))
    ploting(x,y,"Given data")
    ploting(y,res,"Quardratic point with X axis")
    return res
