import sympy as sym
from sympy import *
import string
from sympy.plotting import plot3d
from sympy.plotting import plot3d_parametric_surface
from sympy import Point
from spb import *
import numpy as np
import matplotlib.pyplot as plt
 
print("XXXXXXXXXXXXXXXXXXX")
print("Reeb Graph Computer")
print("XXXXXXXXXXXXXXXXXXX")
#Derivatives of multivariable function

x , y = sym.symbols('x y')
#f = -((4+1-x**2-y**2+(2*2*((1-x**2)**0.5)))**0.5)
#f=((x**2)+(2*2*((1-x**2)**0.5)))**0.5

f=(10-(1*cos(x)))*cos(y)
fx=sin(x)
fy=(10-cos(x))*sin(y)
"""
f=cos(x)*cos(y)
fx=sin(x)*cos(y)
fy=sin(y)
"""
#plot3d_parametric_surface(sin(x)*cos(y), sin(y), cos(x)*cos(y),backend=PB)

#Differentiating partially w.r.t x
derivative_f = f.diff(x)
print(derivative_f)
derivative_fy = f.diff(y)
print(derivative_fy)
critical_point=(sym.solve([derivative_fy,derivative_f,fx,fy], [x, y]))
print(critical_point)
x_values=[]
z_values=[]
for point in range(len(critical_point)):
    z_value=(f.subs([(x, critical_point[point][0]), (y, critical_point[point][1])]))
    x_value=(fx.subs([(x, critical_point[point][0]), (y, critical_point[point][1])]))
    if(z_value in z_values):
        continue
    z_values.append(z_value)
    x_values.append(x_value)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
#print(float(f.subs([(x, 0), (y, pi)])))
#print(str((sym.nonlinsolve([derivative_fy,derivative_f], [x, y]))))

#ii, oo = draw_curve((x_values[0],z_values[0]), (x_values[1],z_values[1]))
# Creating a numpy array
X = np.array(x_values)
Y = np.array(z_values)

# Plotting point using sactter method
plt.scatter(X,Y)

plt.show()