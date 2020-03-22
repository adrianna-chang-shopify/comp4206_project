import numpy as np

# iteration Matrix
A = np.array([10.0/14.0,2.0/14.0,1.0/14.0,1.0/14.0])

# weighted edges matrix
B = np.array([
    [0, 0.8, 0.2, 0],
    [0.5, 0, 0, 0.5],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
])

# Page Rank
for i in range(100):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))