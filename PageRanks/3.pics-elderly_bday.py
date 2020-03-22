# Pics - Elderly bday

# run:
# python 3.pics-elderly_bday.py

import numpy as np

# SUM OUT MATRIX
A = np.array([
    0.4252873563, 0.5402298851, 0, 0, 0, 0, 0, 0, 0, 0, 0.01149425287, 0, 0, 0.02298850575, 0
])

# WEIGHTED EDGE MATRIX
B = np.array([
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.6666666667, 0.08333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0.08333333333, 0, 0, 0.1666666667, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.8, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.5714285714, 0.4285714286, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.08333333333, 0.9166666667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.3333333333, 0.6666666667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.1304347826, 0.8695652174, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA
# A	pics
# B	aww
# C	Austria
# D	CirclingBack
# E	Kanye
# F	OldLadiesBakingPies
# G	Mogong
# H	13or30
# I	discordian
# J	topofreddit
# K	wholesome
# L	Amazing
# M	GetUpvote
# N	PeopleFuckingDying
# O	bruteimpact

# OUTPUT:
# A = 0.357442138121
# B = 0.514046317538
# C = 0.0
# D = 0.0
# E = 0.0
# F = 0.0
# G = 0.0
# H = 0.0
# I = 0.0
# J = 0.0
# K = 0.0428371814403
# L = 0.0
# M = 0.0
# N = 0.0856743629012
# O = 0.0