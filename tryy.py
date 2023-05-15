import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import itertools

fig = plt.figure()
ax = fig.gca(projection='3d')

# plotting the points
pts = [(0,0,0),(1,0,0),(0,2,0),(0,0,3)]
for p in pts:
    ax.scatter(p[0], p[1], p[2], zdir='z', c='r')

# plotting lines for each point pair
for a, b in itertools.product(pts, pts):
    x = np.linspace(a[0], b[0], 100)
    y = np.linspace(a[1], b[1], 100)
    z = np.linspace(a[2], b[2], 100)
    ax.plot(x, y, z)
    

ax.legend()
ax.set_xlim3d(0, 1)
ax.set_ylim3d(0, 2)
ax.set_zlim3d(0, 3)

plt.show()