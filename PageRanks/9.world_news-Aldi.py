# worldnews - Aldi

# run:
# $ python 9.world_news-Aldi.py

import numpy as np

# SUM OUT MATRIX
A = np.array([
    0.7755102041, 0.1020408163, 0, 0.0306122449, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.09183673469, 0
])

# WEIGHTED EDGE MATRIX
B = np.array([
    [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6666666667, 0, 0, 0.1666666667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1666666667, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.125, 0.625, 0, 0.125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.125, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.8723404255, 0.02127659574, 0, 0.02127659574, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.08510638298, 0],
    [0.7142857143, 0.2857142857, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	worldnews
# B	UpliftingNews
# C	traderjoes
# D	ClimateActionPlan
# E	Anticonsumption
# F	ZeroWaste
# G	topofreddit
# H	circular_economy
# I	LegitJustNoMIL
# J	HC_Capitalism
# K	Positive_News
# L	TheAbditory
# M	GreenPartyOfCanada
# N	theworldnews
# O	EcoNewsNetwork
# P	TTAMF

# OUTPUT:
# A = 0.565891472862
# B = 0.32558139534
# C = 0.0
# D = 0.0542635658991
# E = 0.0
# F = 0.0
# G = 0.0
# H = 0.0
# I = 0.0
# J = 0.0
# K = 0.0
# L = 0.0
# M = 0.0
# N = 0.0
# O = 0.0542635658991
# P = 0.0