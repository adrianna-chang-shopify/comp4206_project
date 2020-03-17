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

# initilize iteration matrix
n = 9.0
iterationArray = []
value = 1/n
for i in range(int(n)):
    iterationArray.append(value)

# iteration Matrix
A = np.array([iterationArray])

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
    A = C

print(A)
print(np.sum(A))