# Combined Subreddits - memes

# run:
# $ python 12.combo-memes.py

import numpy as np


# iteration Matrix
A = np.array([
    0.056, 0, 0.2, 0.232, 0.056, 0.008, 0.2213333333, 0.09066666667, 0.12, 0.016
])

# weighted edges matrix
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6, 0, 0.2, 0, 0.2, 0, 0, 0, 0, 0],
    [0.04761904762, 0, 0, 0.2738095238, 0.0119047619, 0.0119047619, 0.3928571429, 0.08333333333, 0.1666666667, 0.0119047619],
    [0.03846153846, 0, 0.2564102564, 0, 0.08974358974, 0.01282051282, 0.358974359, 0.08974358974, 0.141025641, 0.01282051282],
    [0.1428571429, 0, 0.1428571429, 0.1428571429, 0, 0, 0.2142857143, 0, 0.07142857143, 0.2857142857],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.03921568627, 0, 0.3333333333, 0.3137254902, 0.06862745098, 0.009803921569, 0.009803921569, 0.1568627451, 0.06862745098, 0],
    [0.05263157895, 0, 0.05263157895, 0.4210526316, 0, 0, 0.2105263158, 0, 0.2631578947, 0],
    [0.02083333333, 0, 0.3333333333, 0.2708333333, 0.04166666667, 0, 0.2083333333, 0.08333333333, 0.04166666667, 0],
    [0.2, 0, 0, 0.2, 0.6, 0, 0, 0, 0, 0],
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	memes
# B	Blessed_Images
# C	TIHI
# D	awfuleverything
# E	mildlyinfuriating
# F	FellowKids
# G	MakeMeSuffer
# H	thanksihateit
# I	oddlyterrifying
# J	extremelyinfuriating

# OUTPUT:
# A = 0.0584568690412
# B = 0.0
# C = 0.196473004712
# D = 0.22008771947
# E = 0.0604822559829
# F = 0.00785120278897
# G = 0.227627717145
# H = 0.0867708597732
# I = 0.118415832236
# J = 0.023834538852

