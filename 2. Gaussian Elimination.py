# Author: Mehedi Hasan
import numpy as np
import sys

n = int(input("Enter number of equation: "))
a = np.zeros((n, n+1))
x = np.zeros(n)

print("Enter co-efficient of matrix: ")
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input("a[" + str(i+1) + "][" + str(j+1) + "] : "))


print("\nAugmented Matrix: ")
print(a)

# Forward Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - a[i][k] * ratio

print("\nAfter forward elimination")
print(a)

# Back Subtraction
x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

print("\nSolution: ")
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')