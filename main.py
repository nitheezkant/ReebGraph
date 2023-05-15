import sympy as sym
from sympy import *
from spb import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr

print("XXXXXXXXXXXXXXXXXXXX")
print("Reeb Graph Cumputer")
print("XXXXXXXXXXXXXXXXXXXX\n\n")

print("1)Simplecal Complex Specification Method")
print("2)Parametric Function Method to compute critical points")
ch=int(input("Enter option:"))
if ch==1:
    print("Please go through input format, enter it in Input_Points.txt. Z axis will be taken as the Height function.")
    wait=input("Save the txt file and enter any charecter to continue.")
    print()
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
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Original Simplecial Complex")

    fig1 = plt.figure()
    axx = fig1.add_subplot(111, projection='3d')
    axx.set_title("Reeb Graph")
    for i in range(len(x_s)):
        diff=[]
        sign=0
        sign_flips=0
        for j in points[i+1][1]:
            xx=[x_s[i],int(points[int(j)][0][1])]
            yy=[y_s[i],int(points[int(j)][0][2])]
            zz=[z_s[i],int(points[int(j)][0][3])]
            diff=zz[1]-zz[0]
            if diff==0:
                sign_new=sign
            elif diff>0:
                sign_new=1
            else:
                sign_new=-1
            if sign==0:
                pass
            elif sign_new!=sign:
                sign_flips=sign_flips+1
            sign=sign_new
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
            for j in points[i+1][1]:
                if points[int(j)][2]!="reg":
                    for k in points[i+1][1]:
                        if points[int(k)][2]!="reg":
                            xx=[int(points[int(j)][0][1]),int(points[int(k)][0][1])]
                            yy=[int(points[int(j)][0][2]),int(points[int(k)][0][2])]
                            zz=[int(points[int(j)][0][3]),int(points[int(k)][0][3])]
                            axx.plot(xx, yy, zz, c='black')
    #Add all Critical connections
    for i in range(len(x_s)):
        if(points[i+1][2]!="reg"):
            for j in points[i+1][1]:
                if points[int(j)][2]!="reg":
                    xx=[x_s[i],int(points[int(j)][0][1])]
                    yy=[y_s[i],int(points[int(j)][0][2])]
                    zz=[z_s[i],int(points[int(j)][0][3])]
                    axx.plot(xx, yy, zz, c='black')

    X = np.array(saddle_x)
    Y = np.array(saddle_y)
    Z = np.array(saddle_z)
    axx.scatter(X, Y, Z, marker='o',color='blue', label='Blue->Saddle')
    X = np.array(maxima_x)
    Y = np.array(maxima_y)
    Z = np.array(maxima_z)
    axx.scatter(X, Y, Z, marker='o',color='red', label='Red->Maxima')
    X = np.array(minima_x)
    Y = np.array(minima_y)
    Z = np.array(minima_z)
    axx.scatter(X, Y, Z, marker='o',color='green', label='Green->Minima')
    axx.legend()
    axx.grid(True)


    X = np.array(x_s)
    Y = np.array(y_s)
    Z = np.array(z_s)
    ax.scatter(X, Y, Z, c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')
    plt.show()



elif ch==2:
    print("*This option is currently limited to just calculating the critical points.")
    print("1)Custom function")
    print("2)Inbuilt Torus")
    print("3)Inbuilt Spehere")
    u , v = sym.symbols('u v',real=True)
    ch=int(input("Enter the option:"))
    if ch==1:
        print("Make sure you have uncommented the below lines after inserting ur function")
        """
        f= //z function(will be used as height function)
        fx= //x function
        fy= //y function
        u_limu= //u's upper limit(strict)
        v_limu= //v's upper limit(strict)
        u_liml= //u's lower limit(strict)
        v_liml= //v's lower limit(strict)
        """
    elif ch==2:
        r, R = 5, 10
        f=(R-(r*cos(u)))*cos(v)
        fx=r*sin(u)
        fy=(R-(r*cos(u)))*sin(v)
        v_limu=2*pi
        u_limu=2*pi

    elif ch==3:
        f=cos(u)*cos(v)
        fx=sin(u)*cos(v)
        fy=sin(v)
        v_limu=pi/2
        u_limu=2*pi
    print(f,fx,fy,u_limu)
    
    derivative_f = f.diff(u)
    print(derivative_f)
    derivative_fy = f.diff(v)
    print(derivative_fy)
    critical_point=(sym.solve([derivative_fy,derivative_f], [u, v]))
    print(critical_point)
    x_values=[]
    z_values=[]
    y_values=[]
    for point in range(len(critical_point)):
        z_value=(f.subs([(u, critical_point[point][0]), (v, critical_point[point][1])]))
        x_value=(fx.subs([(u, critical_point[point][0]), (v, critical_point[point][1])]))
        y_value=(fy.subs([(u, critical_point[point][0]), (v, critical_point[point][1])]))

        #Out of Domin Rejections
        if critical_point[point][1]>= v_limu:
            continue
        if critical_point[point][0]>= u_limu:
            continue

        if(z_value in z_values):
            continue
        print(critical_point[point][0],critical_point[point][1])
        z_values.append(z_value)
        x_values.append(x_value)
        y_values.append(y_value)
    print(x_values,y_values,z_values)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.array(x_values)
    Y = np.array(y_values)
    Z = np.array(z_values)
    ax.scatter(X, Y, Z, c='r', marker='o')

    if ch==2:
        angle = np.linspace(0, 2 * np.pi, 32)
        v, u= np.meshgrid(angle, angle)
        f = (R + r * np.cos(u)) * np.cos(v)
        fy = (R + r * np.cos(u)) * np.sin(v)
        fx = r * np.sin(u)
        ax.plot_surface(fx, fy, f, color = 'w', rstride = 1, cstride = 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')
    if ch==3:
        angle = np.linspace(0, 2 * np.pi, 32)
        v, u= np.meshgrid(angle, angle)
        f=np.cos(u)*np.cos(v)
        fx=np.sin(u)*np.cos(v)
        fy=np.sin(v)
        ax.plot_surface(fx, fy, f, color = 'w', rstride = 1, cstride = 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')

    plt.show()