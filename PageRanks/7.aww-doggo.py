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

# Results
# C = A.dot(B)

for i in range(100):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))