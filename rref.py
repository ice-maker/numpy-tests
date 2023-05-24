import numpy as np

A = np.array([[4, 3, 6],
              [0, 0, 8],
              [0, 5, 0],
              [6, 1, 1],
              [0, 0, 1],
              [9, 1, -11]]).astype(float)

m = A.shape[0]  # rows
n = A.shape[1]  # cols
sub_row = np.zeros((1, n)).astype(float)
sub_row_i = np.ones((1, m)).astype(float) * -1

# make it so each column only has 1 leading entry
for j in range(np.minimum(m, n)):  # go across cols (constrained by either rows or cols)
    for i in range(m):  # go down rows, find last row with leading entry to subtract from others
        if A[i, j] != 0 and i not in sub_row_i:
            sub_row = A[i] / A[i, j]  # leading entry is 1
            sub_row_i[0, j] = i
    for i in range(m):  # go down rows again, subtract sub_row from rows other than itself and previous sub_rows
        if A[i, j] != 0 and i not in sub_row_i:
            A[i] = A[i] - (sub_row * A[i, j])  # multiply by leading entry of row so it cancels

# make it so pivot positions are the only nonzero entries in their corresponding columns
sub_row = np.zeros((1, n)).astype(float)
sub_row_i = np.ones((1, m)).astype(float) * -1
nonzero = np.zeros(m).astype(int)

for i in range(m):  # go down rows, count entries starting from pivot pos
    nonzero[i] = np.shape(np.trim_zeros(A[i], 'f'))[0]  # number of entries in row starting from pivot pos
nonzero_sort = np.argsort(nonzero).astype(int)

for i in np.flip(nonzero_sort):  # go down rows, subtract rows with fewer leading zeros from each row
    for k in np.flip(nonzero_sort):
        if nonzero[i] > nonzero[k] and A[k, np.minimum(n - nonzero[k], n - 1)] != 0:
            A[i] = A[i] - (A[k] * A[i, np.minimum(n - nonzero[k], n - 1)] / A[k, np.minimum(n - nonzero[k], n - 1)])
    if A[i, np.minimum(n - nonzero[i], n - 1)] != 0:
        A[i] = A[i] / A[i, np.minimum(n - nonzero[i], n - 1)]  # divide so pivot positions are 1

A = np.array(A)[np.flip(nonzero_sort)]  # rewrite the matrix in descending order

print(A)
