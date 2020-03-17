
import numpy as np

# initilize iteration matrix
n = 12.0
iterationArray = []
value = 1/n
for i in range(int(n)):
    iterationArray.append(value)

# iteration Matrix
A = np.array([iterationArray])

# weighted edges matrix
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0],
    [0.3333333333, 0, 0, 0, 0, 0.3333333333, 0, 0, 0, 0.3333333333, 0, 0],
    [0.8333333333, 0, 0, 0.1666666667, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6666666667, 0, 0, 0, 0, 0.3333333333, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Results
# C = A.dot(B)

for i in range(100):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))