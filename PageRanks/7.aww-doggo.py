# aww - Doggo

# run:
# python 7.aww-doggo.py

import numpy as np

# SUM OUT MATRIX
A = np.array([
    0.9285714286, 0, 0, 0, 0.03571428571, 0, 0, 0.03571428571, 0, 0, 0, 0, 0
])

# WEIGHTED EDGE MATRIX
B = np.array([
[0, 0, 0, 0, 0.5, 0, 0, 0.5, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	aww
# B	hitmanimals
# C	KittyPupperLove
# D	CatsWithDogs
# E	PeopleFuckingDying
# F	shiba
# G	Thisismylifemeow
# H	cats
# I	TheCuddlePuddle
# J	Animalsbeingbeds
# K	Cuteanimalsdailyshow
# L	delola3100
# M	oddcouples

# OUTPUT
# A = 0.928571428581
# B = 0.0
# C = 0.0
# D = 0.0
# E = 0.0357142857093
# F = 0.0
# G = 0.0
# H = 0.0357142857093
# I = 0.0
# J = 0.0
# K = 0.0
# L = 0.0
# M = 0.0