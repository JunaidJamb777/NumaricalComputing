import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def builtin(x,y,X):
    f = interp1d(x, y)
    y_hat = f(X)
    print(y_hat)
    plt.style.use('seaborn-poster')
    plt.figure(figsize = (10,8))
    plt.plot(x, y, '-ob')
    plt.plot(X,y_hat)
    plt.title('Linear Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def plot(x,y,point):
    plt.style.use('seaborn-poster')
    plt.figure(figsize = (10,8))
    plt.plot(x, y, '-ob')
    plt.plot(point,linear_inter(x,y,point) , 'ro')
    plt.title('Linear Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def linear_inter(x,y,point):
    # f1(x)=y0 +((y1 -y0)/(x1 -x0) )(x-x0)
    a=((y[1] - y[0])/(x[1] -x[0]) )
    point=y[0] + a * (point-x[0])
    print('f1(x)=y0 +((y1 -y0)/(x1 -x0) )(x-x0)',point)
    return point
