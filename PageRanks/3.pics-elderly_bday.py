# Pics - Elderly bday

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

# run:
# python 3.pics-elderly_bday.py

import numpy as np

# initilize iteration matrix
n = 15.0
iterationArray = []
value = 1/n
for i in range(int(n)):
    iterationArray.append(value)

# iteration Matrix
A = np.array([iterationArray])

# weighted edges matrix
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

# Results
# C = A.dot(B)

for i in range(100):
    C = A.dot(B)
    A = C

print(A)
print(np.sum(A))