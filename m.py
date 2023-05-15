import sympy as sym
from sympy import *
from spb import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
x , y, z = sym.symbols('x y z',real=True)
ipt=open("Input_Points.txt")
points={}
x_s=[]
y_s=[]
z_s=[]
regular_x=[]
regular_y=[]
regular_z=[]

saddle_x=[]
saddle_y=[]
saddle_z=[]

maxima_x=[]
maxima_y=[]
maxima_z=[]

minima_x=[]
minima_y=[]
minima_z=[]
while True:
    point=ipt.readline().split()
    if point[0]=="x":
        break
    x_s.append(int(point[1]))
    y_s.append(int(point[2]))
    z_s.append(int(point[3]))
    edges=ipt.readline().split()
    points[int(point[0])]=[point,edges]
print(points)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

fig1 = plt.figure()
axx = fig1.add_subplot(111, projection='3d')
for i in range(len(x_s)):
    diff=[]
    sign=0
    sign_flips=0
    for j in points[i+1][1]:
        #print(j)
        xx=[x_s[i],int(points[int(j)][0][1])]
        yy=[y_s[i],int(points[int(j)][0][2])]
        zz=[z_s[i],int(points[int(j)][0][3])]
        diff=zz[1]-zz[0]
        print(sign)
        if diff>=0:
            sign_new=1
        else:
            sign_new=-1
        if sign==0:
            pass
        elif sign_new!=sign:
            sign_flips=sign_flips+1
        sign=sign_new
        print(xx,yy,zz)
        ax.plot(xx, yy, zz, c='r', marker='o')
    if sign_flips==0:
        if sign ==1:
            #Minima
            print("min",points[i+1][0])
            minima_x.append(x_s[i])
            minima_y.append(y_s[i])
            minima_z.append(z_s[i])
            points[i+1].append("min")
        else:
            print("max",points[i+1][0])
            maxima_x.append(x_s[i])
            maxima_y.append(y_s[i])
            maxima_z.append(z_s[i])
            points[i+1].append("max")
    elif sign_flips>2:
        print("saddle",points[i+1][0])
        saddle_x.append(x_s[i])
        saddle_y.append(y_s[i])
        saddle_z.append(z_s[i])
        points[i+1].append("sad")
    else:
        print("reg",points[i+1][0])
        regular_x.append(x_s[i])
        regular_y.append(y_s[i])
        regular_z.append(z_s[i])
        points[i+1].append("reg")
#Remove Regular Points
for i in range(len(x_s)):
    if(points[i+1][2]=="reg"):
        print("redd", i+1)
        for j in points[i+1][1]:
            if points[int(j)][2]!="reg":
                 print(["c1",int(j)])
                 for k in points[i+1][1]:
                     if points[int(k)][2]!="reg":
                        print(["c2",int(k)])
                        print("hi",int(k))
                        xx=[int(points[int(j)][0][1]),int(points[int(k)][0][1])]
                        yy=[int(points[int(j)][0][2]),int(points[int(k)][0][2])]
                        zz=[int(points[int(j)][0][3]),int(points[int(k)][0][3])]
                        axx.plot(xx, yy, zz, c='black')
#Add all Critical connections
for i in range(len(x_s)):
    if(points[i+1][2]!="reg"):
        print(i+1)
        for j in points[i+1][1]:
            if points[int(j)][2]!="reg":
                xx=[x_s[i],int(points[int(j)][0][1])]
                yy=[y_s[i],int(points[int(j)][0][2])]
                zz=[z_s[i],int(points[int(j)][0][3])]
                axx.plot(xx, yy, zz, c='black')

X = np.array(saddle_x)
Y = np.array(saddle_y)
Z = np.array(saddle_z)
axx.scatter(X, Y, Z, marker='o',color='blue')
X = np.array(maxima_x)
Y = np.array(maxima_y)
Z = np.array(maxima_z)
axx.scatter(X, Y, Z, marker='o',color='red')
X = np.array(minima_x)
Y = np.array(minima_y)
Z = np.array(minima_z)
axx.scatter(X, Y, Z, marker='o',color='green')


X = np.array(x_s)
Y = np.array(y_s)
Z = np.array(z_s)
ax.scatter(X, Y, Z, c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')
plt.show()



