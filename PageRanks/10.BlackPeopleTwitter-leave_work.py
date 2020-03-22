# BlackPeopleTwitter - leave work

# run:
# $ python 10.BlackPeopleTwitter-leave_work.py


import numpy as np

# iteration Matrix
A = np.array([
    0.7826086957, 0, 0, 0.04347826087, 0, 0.08695652174, 0, 0, 0.04347826087, 0.04347826087, 0, 0
])

# weighted edges matrix
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0],
    [0.3333333333, 0, 0, 0, 0, 0.3333333333, 0, 0, 0, 0.3333333333, 0, 0],
    [0.8333333333, 0, 0, 0.1666666667, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.6666666667, 0, 0, 0, 0, 0.3333333333, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	BlackPeopleTwitter
# B	electricians
# C	nursing
# D	walmart
# E	starbucks
# F	KitchenConfidential
# G	bartenders
# H	Snorkblot
# I	antiwork
# J	topofreddit
# K	mistyfront
# L	CinnamonToastKen

# OUTPUT:
# A = 0.0
# B = 0.0
# C = 0.0
# D = 0.0
# E = 0.0
# F = 0.0
# G = 0.0
# H = 0.0
# I = 0.0
# J = 0.0
# K = 0.0
# L = 0.0
