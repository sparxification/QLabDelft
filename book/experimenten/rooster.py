#%matplotlib qt

from ipywidgets import interact
from ipywidgets import IntSlider
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from itertools import product, combinations

coordinates = np.array([
    [0.5, 0, 0.0], [0, 0.5, 0.0], [1, 0.5, 0.0], [0.5, 1, 0.0],
    [0.25, 0.75, 0.25],
    [0, 0, 0.5], [1, 0, 0.5], [0, 1, 0.5], [1, 1, 0.5],
    [0.25, 0.25, 0.75], [0.75, 0.75, 0.75], 
    [0.5, 0, 1], [0, 0.5, 1], [1, 0.5, 1], [0.5, 1, 1],
])

#Set the location of the NV center
N = np.array([0.75, 0.25, 0.25])
V = np.array([0.5, 0.5, 0.5])

def plot_atoms(elev, azim):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot spheres with dark grey outline and lighter grey fill
    for coord in coordinates:
        if np.all(coord == [0.5, 0.5, 0.5]):
            ax.scatter(coord[0], coord[1], coord[2], color='none', edgecolor='black', linestyle='dashed', s=200)
        else:
            ax.scatter(coord[0], coord[1], coord[2], color='dimgrey', edgecolor='black', s=200)

    # Plot blue sphere for N and dashed circumference for V
    ax.scatter(N[0], N[1], N[2], color='blue', edgecolor='black', s=200)
    ax.scatter(V[0], V[1], V[2], color='w', edgecolor='black', s=200)

    # Function to calculate Euclidean distance between two points
    def distance(point1, point2):
        return np.linalg.norm(point1 - point2)

    # Function to find nearest neighbors for each atom
    def find_nearest_neighbors(coords, threshold):
        nearest_neighbors = []
        for i, atom1 in enumerate(coords):
            for j, atom2 in enumerate(coords):
                if j > i:  # Avoid checking distances twice
                    if distance(atom1, atom2) <= threshold:
                        nearest_neighbors.append((i, j))
        return nearest_neighbors

    # Find nearest neighbors among the atoms
    nearest_neighbors = find_nearest_neighbors(np.concatenate((coordinates, [V], [N]), axis=0), threshold=0.6)  # Adjust threshold as needed

    # Plot lines between nearest neighbors
    for pair in nearest_neighbors:
        atom1 = np.concatenate((coordinates, [V], [N]), axis=0)[pair[0]]
        atom2 = np.concatenate((coordinates, [V], [N]), axis=0)[pair[1]]
        if np.any(atom1 == V) or np.any(atom2 == V) or np.any(atom1 == N) or np.any(atom2 == N):
            # Plot dashed lines for connections involving the NV centers
            ax.plot([atom1[0], atom2[0]], [atom1[1], atom2[1]], [atom1[2], atom2[2]], color='green', linestyle='dashed')
        else:
            ax.plot([atom1[0], atom2[0]], [atom1[1], atom2[1]], [atom1[2], atom2[2]], color='green')

    # Plot dashed cube around data points
    for s, e in combinations(np.array(list(product([0, 1], repeat=3))), 2):
        if np.sum(np.abs(s-e)) == 1:
            ax.plot3D(*zip(s, e), color="b", linestyle='dashed')

    ax.view_init(elev=elev, azim=azim)
    ax.set_proj_type('ortho')
    ax.set_box_aspect([1,1,1])  # Set aspect ratio
    
    plt.axis('off')

    plt.show()

plot_atoms(12,82)