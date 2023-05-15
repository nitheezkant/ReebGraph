import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gudhi

# Define the function f(u,v) = cos(u)*cos(v)
def f(u,v):
    return np.cos(u)*np.cos(v)

# Define the domain
u = np.linspace(-2*np.pi, 2*np.pi, 100)
v = np.linspace(-2*np.pi, 2*np.pi, 100)
U,V = np.meshgrid(u,v)

# Evaluate the function on the domain
Z = f(U,V)

# Initialize the alpha complex with the function values
alpha_complex = gudhi.AlphaComplex(points=np.column_stack([U.flatten(), V.flatten(), Z.flatten()]))
alpha_complex.create_simplex_tree()

# Compute the Reeb graph
persistence = alpha_complex.persistence()
diagrams = gudhi.plot_persistence_diagram(persistence)
gudhi.plot_persistence_barcode(persistence)
plt.show()

# Plot the Reeb graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
gudhi.plot_persistence_barcodes(persistence, ax=ax)
plt.show()
