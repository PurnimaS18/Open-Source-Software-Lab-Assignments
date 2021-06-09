# Create two matrices with 2x2 dimensions. Initialize them with values [4,5], [3,2]. Calculate
# determinant of a two-dimensional matrix using scipy.linalg. Calculate the inverse of a matrix
# in 3.
import numpy as np
from scipy import linalg
A = np.array([[4, 5], [3, 2]])
print(A)
print(linalg.det(A)) # determinanat
print(linalg.inv(A)) # inverse