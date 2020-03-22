# Pics - HK Protesters

# run: 
# $ python 2.pics-HK_protesters.py

import numpy as np

# SUM OUT MATRIX
A = np.array([28.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0,	2.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0])

# WEIGHTED EDGE MATRIX
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.3333333333, 0, 0, 0, 0.6666666667, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
# for i in range(len(A)):
#     print(str(A[i]))

# FOR TROUBLESHOOTING
# print(np.sum(A))

# DATA:
# A	pics
# B	ShitLiberalsSay
# C	no_sob_story
# D	FreeHongKongNow
# E	HongKongProtest
# F	topofreddit
# G	TheFightThatMatters
# H	LIHKG
# I	Flagblack

# OUTPUT:
# A = 0.0
# B = 0.0
# C = 0.0
# D = 0.0
# E = 0.0
# F = 0.0
# G = 0.0
# H = 0.0
# I = 0.0