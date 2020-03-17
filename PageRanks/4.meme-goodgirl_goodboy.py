# NEED TO FIX



import numpy as np

# initilize iteration matrix
n = 10.0
iterationArray = []
value = 1/n
for i in range(int(n)):
    iterationArray.append(value)

# iteration Matrix
A = np.array([iterationArray])

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

# Results
# C = A.dot(B)

for i in range(1):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))