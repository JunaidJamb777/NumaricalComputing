import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

def builtin(x,y,p1,p2,p3):
    P1 = poly.Polynomial(p1)
    P2 = poly.Polynomial(p2)
    P3 = poly.Polynomial(p3)
    a=[P1,P2,P3]
    x_new = np.arange(-1.0, 3.1, 0.1)

    fig = plt.figure(figsize = (10,8))
    plt.plot(x_new, P1(x_new), 'b', label = 'P1')
    plt.plot(x_new, P2(x_new), 'r', label = 'P2')
    plt.plot(x_new, P3(x_new), 'g', label = 'P3')

    plt.plot(x, np.ones(len(x)), 'ko', x, np.zeros(len(x)), 'ko')
    plt.title('Lagrange Basis Polynomials')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()
    return a
# builtin(x,y,P1_coeff,P2_coeff,P3_coeff)

x = [0, 1, 2]
y = [1, 3, 2]
P1_coeff = [1,-1.5,.5]
P2_coeff = [0, 2,-1]
P3_coeff = [0,-.5,.5]
def plot(x,y):
    plt.figure(figsize = (10,8))
    plt.plot(x,y, '-ob')
    plt.title('Linear Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return True

def fx(x,y,p):
    a=((y[1] - y[0])/(x[1] -x[0]) )
    point=y[0] + a * (p - x[0])
    print('f1(x)=y0 +((y1 -y0)/(x1 -x0) )(x-x0)',point)
    return point

def f(xi,xj,point):
    res=[]
    x0=xi[0]
    y0=xi[0]
    p=point[0]
    for i in range(1,len(xi)):
        x1=xi[i]
        y1=xj[i]
        p=float(point[i])
        x=[x0,x1]
        y=[y0,y1]
        print(x,y,p)
        res.append(fx(x,y,p))
        print(fx(x,y,p))
        x0=x1
        y0=y1

    return res