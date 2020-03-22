# Pics - Llama at wedding

# A	pics
# B	Judaism
# C	Jewdank
# D	UnexpectedlyWholesome
# E	schnozcheck
# F	topofreddit
# G	OPDelivers
# H	casualllama
# I	no_sob_story
# J	aww
# K	MxRMods
# L	llama
# M	KarmaConspiracy
# N	memesthatbigdank

# run:
# python 5.pics-llama_at_weding.py

import numpy as np

# iteration Matrix
A = np.array([
    0.8913043478, 0.02173913043, 0, 0, 0, 0, 0, 0, 0, 0.08695652174, 0, 0, 0, 0
])

# weighted edges matrix
B = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6666666667, 0, 0, 0.3333333333, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.3333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0.6666666667, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Page Rank
for i in range(100):
    C = A.dot(B)
    A = C/C.sum(axis=0,keepdims=1)

print(A)
print(np.sum(A))