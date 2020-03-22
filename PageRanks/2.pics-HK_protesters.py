# Pics - HK Protesters

# A	pics
# B	ShitLiberalsSay
# C	no_sob_story
# D	FreeHongKongNow
# E	HongKongProtest
# F	topofreddit
# G	TheFightThatMatters
# H	LIHKG
# I	Flagblack

# run: 
# $ python 2.pics-HK_protesters.py

import numpy as np

# iteration Matrix
A = np.array([28.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0,	2.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0,	0.0/30.0])

# weighted edges matrix
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

# Results

for i in range(1):
    C = A.dot(B)
    A = C/C.sum(axis=0,keepdims=1)

print(A)
print(np.sum(A))

# OUTPUT:
