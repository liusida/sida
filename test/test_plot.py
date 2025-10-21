import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "src"))
import sida.plot
import numpy as np

# Create a sample matrix with positive and negative values
matrix = np.random.randn(5, 5) * 10

# Plot the matrix
fig, ax = sida.plot.plot_matrix(matrix, title="Sample Matrix")
fig.show()