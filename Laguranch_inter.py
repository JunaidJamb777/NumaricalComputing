import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def lagurang_poly(x,y,p1_coeff,p2_coeff,p3_coeff):
    # get the polynomial function
    P1 = poly.Polynomial(p1_coeff)
    P2 = poly.Polynomial(p2_coeff)
    P3 = poly.Polynomial(p3_coeff)

    x_new = np.arange(-1.0, 3.1, 0.1)

    fig = plt.figure(figsize = (10,8))
    plt.plot(x_new, P1(x_new), 'b', label = 'P1')
    plt.plot(x_new, P2(x_new), 'r', label = 'P2')
    plt.plot(x_new, P3(x_new), 'g', label = 'P3')

    plt.plot(x, np.ones(len(x)), 'bo', x, np.zeros(len(x)), 'ko')
    plt.title('Lagrange Basis Polynomials')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.show()
