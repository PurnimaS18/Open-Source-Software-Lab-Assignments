# Define two-dimensional array with values {(5,4),(6,3)}. Output eigen values and
# eigenvectors of the matrix.

import numpy as np
from scipy import linalg
x = np.array([[5,4], [6,3]])

eigval, eigvec = linalg.eig(x)
print(eigval)
print("\n")
print(eigvec)
