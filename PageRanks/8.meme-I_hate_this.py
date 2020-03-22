# Memes - I hate this

# run:
# $ python 8.meme-I_hate_this.py

import numpy as np

# iteration Matrix
A = np.array([
    0.1918604651, 0.1918604651, 0.2209302326, 0, 0.01744186047, 0.01744186047, 0.2441860465, 0.0523255814, 0, 0, 0.05813953488, 0, 0, 0.005813953488, 0
])

# weighted edges matrix
B = np.array([
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0.06666666667, 0.1777777778, 0.2666666667, 0, 0, 0.02222222222, 0.3555555556, 0.04444444444, 0, 0, 0.06666666667, 0, 0, 0, 0],
[0.08333333333, 0, 0, 0, 0.125, 0.04166666667, 0.7083333333, 0, 0, 0, 0.04166666667, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.5, 0, 0, 0, 0, 0, 0.25, 0, 0, 0, 0, 0, 0, 0.25, 0],
[0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.075, 0.425, 0.3, 0, 0, 0.025, 0.025, 0.075, 0, 0, 0.075, 0, 0, 0, 0],
[0.2307692308, 0, 0.4615384615, 0, 0, 0, 0.07692307692, 0, 0, 0, 0.2307692308, 0, 0, 0, 0],
[0.5, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.04545454545, 0.3181818182, 0.3181818182, 0, 0, 0, 0.2272727273, 0.09090909091, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0.9166666667, 0, 0.08333333333, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
for i in range(len(A)):
    print(D[i] + " = " + str(A[i]))

# FOR THE DATA INPUT INTO SPREADSHEET:
for i in range(len(A)):
    print(str(A[i]))

# FOR TROUBLESHOOTING
print(np.sum(A))

# DATA:
# A	memes
# B	TIHI
# C	awfuleverything
# D	deepfrieddiagrams
# E	mildlyinfuriating
# F	FellowKids
# G	MakeMeSuffer
# H	thanksihateit
# I	void_memes
# J	school_memes
# K	oddlyterrifying
# L	OG_Autobauer
# M	CinnamonToastKen
# N	extremelyinfuriating
# O	RamnagaraRagiMuddhes

# OUTPUT:
# A = 0.112256251274
# B = 0.166323539594
# C = 0.207807694355
# D = 0.0
# E = 0.0259759617939
# F = 0.0185144210475
# G = 0.246387538335
# H = 0.144636901394
# I = 0.0
# J = 0.0
# K = 0.0716037017594
# L = 0.0
# M = 0.0
# N = 0.00649399044836
# O = 0.0