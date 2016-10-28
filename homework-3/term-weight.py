import numpy as np

term_frequency = np.matrix([
    [7, 2, 7, 7, 3],
    [4, 5, 8, 2, 4],
    [1, 5, 0, 0, 7],
    [1, 3, 3, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 3, 0, 0, 0],
    [3, 0, 0, 0, 0],
    [0, 1, 2, 0, 0],
    [3, 0, 1, 0, 0],
    [0, 0, 1, 0, 2]
    ])

maximum_freq_of_doc = term_frequency.max(axis=0)
# print(maximum_freq_of_doc[0,0])
# a = np.count_nonzero(term_frequency[:,0])
# number_of_term = np.count_nonzero(term_frequency[:,0])
row, column = term_frequency.shape
distict_term_available = np.zeros(shape=(1,column))
for i in range(column):
    distict_term_available[0,i] = np.count_nonzero(term_frequency[:,i])


"""
ITF Cal
"""
itf = np.empty_like(distict_term_available)
for i in range(column):
    itf[0,i] = np.log2( 10 / distict_term_available[0,i] )
with open('itf-cal.csv', 'w') as itff:
    itff.write("one,two,three,four,five\n")
    itff.write(
            "{:.4f},{:.4f},{:.4f},{:.4f},{:.4f}".format(
                float(itf[0,0]), float(itf[0,1]), float(itf[0,2]), float(itf[0,3]), float(itf[0,4])
                ))
itff.close()
print("ITF Value" + "=" * 20)
print(itf)

"""
Weight
"""
itf_square = np.square(itf)
def above_weight(i, j):
    p = (0.5 + 0.5 * term_frequency[i,j]/maximum_freq_of_doc[0,j]) * itf[0,j]
    return p 

# print(np.square(itf))
above_eq = np.zeros(shape=(row,column))
for i in range(row):
    for j in range(column):
        above_eq[i,j] = above_weight(i,j)

with open('above-eq.csv', 'w') as abeq:
    abeq.write("one,two,three,four,five\n")
    i = 1
    for i in range(row):
        msg = "{:.4f},{:.4f},{:.4f},{:.4f},{:.4f}\n".format(above_eq[i,0], above_eq[i,1], above_eq[i,2], above_eq[i,3], above_eq[i,4])
        abeq.write(msg)
