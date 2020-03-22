# aww - Doggo

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

# run:
# python 7.aww-doggo.py

import numpy as np

# iteration Matrix
A = np.array([
    0.9285714286, 0, 0, 0, 0.03571428571, 0, 0, 0.03571428571, 0, 0, 0, 0, 0
])

# weighted edges matrix
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

# Page Rank
for i in range(100):
    C = A.dot(B)
    A = C/C.sum(axis=0,keepdims=1)

print(A)
print(np.sum(A))