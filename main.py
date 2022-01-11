import numpy as np
import Linear_Interpolution as LI
def Linear():
    x = [ 1, 2]
    y = [ 3, 2]
    X=1.5
    LI.linear_inter(x,y,X)
    LI.plot(x,y,X)

import Quadratic_inter as QI
def Quadratic():
    x = [1, 4, 8, 12, 11, 9, 7, 5, 3]
    y = [1, 3, 6, 10, 13, 11, 8, 5, 3]
    y_new=QI.Qd_inter(x,y,9,1.5)
    x_new = np.linspace(0,20,100)
    # QI.ploting(x,y,"sample")

import poly_Inter as PI
def polynomial():
    x=[2,6,3,9,1]
    y=[3,6,8,7,2]
    p=[4.2,3.33,4,5,6,7]
    PI.f(x,y,p)
    PI.plot(x,y)

import Laguranch_inter as LIP
def lagranch():
    x = [0, 1, 2]
    y = [1, 3, 2]
    P1_coeff = [1,-1.5,.5]
    P2_coeff = [0, 2,-1]
    P3_coeff = [0,-.5,.5]
    LIP.lagurang_poly(x,y,P1_coeff,P2_coeff,P3_coeff)

import Newtons_inter as NI
def Newtons():
    x = np.array([-5, -1, 0, 2])
    y = np.array([-2, 6, 1, 3])
    NI.Newtons(x,y)






