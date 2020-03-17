# Pics - Texan resto 

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

# run: 
# $ python 1.pics-texas_resto.py

import numpy as np

# initilize iteration matrix
n = 13.0
iterationArray = []
value = 1/n
for i in range(int(n)):
    iterationArray.append(value)

# iteration Matrix
A = np.array([iterationArray])

# weighted edges matrix
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

# Results
# C = A.dot(B)

for i in range(100):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))