# NEED TO FIX

import numpy as np

# iteration Matrix
A = np.array([
    0.9411764706, 0, 0, 0, 0, 0, 0, 0, 0, 0.05882352941
])

# weighted edges matrix
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0.2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Page Rank
for i in range(100):
    C = A.dot(B)
    A = C/C.sum(axis=0,keepdims=1)

print(A)
print(np.sum(A))