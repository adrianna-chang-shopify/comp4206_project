# Pics - Texan resto 

# run: (once in proper directory)
# $ python 1.pics-texas_resto.py

import numpy as np

# SUM OUT MATRIX
A = np.array([32.0/40.0,	1.0/40.0,	0.0/40.0,	1.0/40.0,	0.0/40.0,	0.0/40.0,	6.0/40.0,	0.0/40.0,	0.0/40.0,	0.0/40.0,	0.0/40.0,	0.0/40.0,	0.0/40.0])

# WEIGHTED EDGE MATRIX
B = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.25, 0, 0, 0, 0, 0, 0.75, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.923076923076923, 0, 0, 0, 0, 0, 0.0769230769230769, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

# PAGE RANK ALGO
for i in range(100):
    C = A.dot(B)
    A = C/C.sum(axis=0,keepdims=1)

# FOR OUTPUTTING RESULT
A = [float(x) for x in A]

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
# for i in range(len(A)):
#     print(str(A[i]))

# FOR TROUBLESHOOTING
# print(np.sum(A))

# DATA:
# A	pics
# B	texas
# C	HelloInternet
# D	antiwork
# E	no_sob_story
# F	Anarcho_Capitalism
# G	ABoringDystopia
# H	topofreddit
# I	fairwage
# J	goodpraxis
# K	EndTipping
# L	mutualism
# M	Shitstatistssay

# OUTPUT:
# A = 0.845
# B = 0.155
# C = 0.0
# D = 1.25748668462e-23
# E = 0.0
# F = 0.0
# G = 7.54492010771e-23
# H = 0.0
# I = 0.0
# J = 0.0
# K = 0.0
# L = 0.0
# M = 0.0