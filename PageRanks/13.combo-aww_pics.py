# Combined Subreddts - aww + pics

# run:
# $ python 13.combo-aww_pics.py

import numpy as np

# iteration Matrix
A = np.array([
    0.42, 0.06, 0.18, 0.2733333333, 0.006666666667, 0.02, 0.02, 0, 0.006666666667, 0, 0.01333333333
])

# weighted edges matrix
B = np.array([
[0, 0.1568627451, 0.4901960784, 0.3333333333, 0, 0, 0, 0, 0.01960784314, 0, 0],
[0.8484848485, 0, 0.0303030303, 0.1212121212, 0, 0, 0, 0, 0, 0, 0],
[0.95, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.625, 0, 0.125, 0, 0.125, 0, 0, 0, 0, 0, 0.125],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.25, 0, 0, 0.75, 0, 0, 0, 0],
[0, 0, 0, 0.5714285714, 0, 0.4285714286, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0.625, 0, 0, 0.375, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0.125, 0, 0, 0.75, 0, 0, 0, 0, 0, 0, 0.125],
])

# PAGE RANK ALGO
for i in range(100):
    C = A.dot(B)
    # A = C/C.sum(axis=0,keepdims=1)
    sums = C.sum(axis=0,keepdims=1)
    sums[sums==0] = 1
    A = C/sums

# FOR OUTPUTTING RESULT
A = [float(x) for x in A]

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	aww
# B	PeopleFuckingDying
# C	cats
# D	pics
# E	texas
# F	antiwork
# G	ABoringDystopia
# H	HongKongProtest
# I	wholesome
# J	Judaism
# K	KarmaConspiracy

# OUTPUT:
# A = 0.423983060789
# B = 0.0782704202175
# C = 0.23526545205
# D = 0.200470278242
# E = 0.0250587844166
# F = 4.52120191716e-27
# G = 4.52120191716e-27
# H = 0.0
# I = 0.00831339347154
# J = 0.0
# K = 0.0286386108135


