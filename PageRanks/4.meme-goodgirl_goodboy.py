# Meme - Good girl good boy

# run: 
# $ python 4.meme-goodgirl_goodboy.py

import numpy as np

# SUM OUT MATRIX
A = np.array([
    0.9411764706, 0, 0, 0, 0, 0, 0, 0, 0, 0.05882352941
])

# WEIGHTED EDGE MATRIX
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.8, 0, 0, 0, 0, 0, 0, 0, 0, 0.2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
# for i in range(len(A)):
#     print(str(A[i]))

# FOR TROUBLESHOOTING
# print(np.sum(A))

# DATA:
# A	memes
# B	vegan
# C	antimeme
# D	VetTech
# E	AntiVegan
# F	bonehealingjuice
# G	rawpetfood
# H	simplydogs
# I	wholesome
# J	Blessed_Images

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