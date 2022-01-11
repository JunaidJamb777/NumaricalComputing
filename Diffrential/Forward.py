import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

print('EXAMPLE: Consider the function f(x)=cos(x). We know the derivative of cos(x) is −sin(x). Although in practice we may not know the underlying function we are finding the derivative for, we use the simple example to illustrate the aforementioned numerical differentiation methods and their accuracy. The following code computes the derivatives numerically.')

# my_fun(f,a,b,n)
def my_fun():
    # step size
    h = 0.1
    # define grid
    x = np.arange(0, 2*np.pi, h) 
    # compute function
    y = np.cos(x) 
    print("X ",x," Y ",y)
    # compute vector of forward differences
    forward_diff = np.diff(y)/h 
    backward_diff = (np.diff(y)/h)-0.1
    central_diff = (np.diff(y)/h)/2

    # compute corresponding grid
    xf_diff = x[:-1:]
    xb_diff = x[:-1:]
    xc_diff = x[:-2:] 

    # compute exact solution
    exact_solution = -np.sin(xb_diff) 

    # Plot solution
    plt.figure(figsize = (12, 8))
    plt.plot(xb_diff, backward_diff, '--', \
            label = 'Finite difference approximation')
    plt.plot(xb_diff, exact_solution, \
            label = 'Exact solution')
    plt.legend()
    plt.show()

    # Compute max error between 
    # numerical derivative and exact solution
    max_error = max(abs(exact_solution - forward_diff))
    print(max_error)
my_fun()