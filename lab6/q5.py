# Create Sparse matrices A and B and analyze various functions of sciPy sparse package

import numpy as np
from scipy import sparse

A = np.array([[0, 0], [0, 1], [3, 0]])
B = np.array([[0, 2, 0], [2, 0, 1], [0, 3, 0]])

mat_spa_A = sparse.csr_matrix(A)
mat_spa_B = sparse.csr_matrix(B)

print(mat_spa_A)
print('\n')
print(mat_spa_B)
print('\n')
print(sparse.eye(3,4))
print('\n')
print(sparse.identity(4))
print('\n')
print(sparse.issparse(B))
print('\n')