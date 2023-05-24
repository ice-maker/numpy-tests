import numpy as np

x = np.array([1, -1, 2, -3])  # x values of points to interpolate
y = np.array([29, -35, 31, -19])  # y values of points to interpolate

n = x.size

# numpy has a built-in function for making vandermonde matrices, but I did it manually for learning purposes
A = [np.ones(n)]  # entries of x raised to zeroth power
for i in range(n - 1):
    A = np.insert(A, 0, [np.power(x, i + 1)], axis=0)  # inserted so coefficients are in descending order
A = np.transpose(A)  # powers should increase along rows, not along columns

# solve for coefficients
B = np.linalg.solve(A, y)

print("the coefficients for the interpolating polynomial in descending order are", B)
