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
    A = C/C.sum(axis=0,keepdims=1)

A = [float(x) for x in A]

# D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

# for i in range(len(A)):
#     print(D[i] + " = " + str(A[i]))

for i in range(len(A)):
    print(str(A[i]))

# Confirming 
print(np.sum(A))