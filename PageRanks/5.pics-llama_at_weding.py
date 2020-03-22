# Pics - Llama at wedding

# run:
# python 5.pics-llama_at_weding.py

import numpy as np

# SUM OUT MATRIX
A = np.array([
    0.8913043478, 0.02173913043, 0, 0, 0, 0, 0, 0, 0, 0.08695652174, 0, 0, 0, 0
])

# WEIGHTED EDGE MATRIX
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6666666667, 0, 0, 0.3333333333, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.3333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0.6666666667, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
# print(np.sum(A))

# DATA:
# A	pics
# B	Judaism
# C	Jewdank
# D	UnexpectedlyWholesome
# E	schnozcheck
# F	topofreddit
# G	OPDelivers
# H	casualllama
# I	no_sob_story
# J	aww
# K	MxRMods
# L	llama
# M	KarmaConspiracy
# N	memesthatbigdank

# OUTPUT:
# A = 0.898550724637
# B = 1.71491501102e-32
# C = 0.0
# D = 0.0
# E = 0.0
# F = 0.0
# G = 0.0
# H = 0.0
# I = 0.0
# J = 0.0676328502454
# K = 0.0
# L = 0.0
# M = 0.0338164251176
# N = 0.0