
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Taking user input ~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    try:
        N = int(input("Enter the Number of Points: "))
        if N > 1: break
        else: print("Number of Points must be greater than 1")
    except ValueError:
        print("Enter a Natural Number greater than 1")
X, Y = [], []
for i in range(N):
    while True:
        try:
            x = float(input("Enter the X coordinate of the point "+str(i+1)+": "))
        except ValueError:
                print("Enter a Real Number")
                continue
        else: break
    X.append(x)
    while True:
        try:
            y = float(input("Enter the Y coordinate of the point "+str(i+1)+": "))
        except ValueError:
                print("Enter a Real Number")
                continue
        else: break
    Y.append(y)
while True:
    try:
        n = int(input("Enter the Degree of polynomial: "))
        if n > 0: break
        else: print("Degree of polynomial must be greater than 1")
    except ValueError:
        print("Enter a Natural Number greater than 0")
print()

from numpy import array, zeros, linalg


# X = [0, 1, 2, 3, 4, 5]      # numpy.arange(6)
# Y = [2, 8, 14, 28, 39, 62]

X = array(X, float)
Y = array(Y, float)

N = len(X)  # Number of data points
n = 2       # Degree of polynomial
# n = 3


# [A]{a} = {B}
A = zeros((n+1, n+1))
B = zeros(n+1)
a = zeros(n+1)


#     [   N     ∑ xi      ∑ xi^2    ∑ xi^n   ]      [∑      yi]
# A = [ ∑ xi    ∑ xi^2    ∑ xi^3    ∑ xi^n+1 ], B = [∑ xi   yi]
#     [ ∑ xi^n  ∑ xi^n+1  ∑ xi^n+2  ∑ xi^2n  ]      [∑ xi^n yi]

# A[row, col] = ∑ xi^(row+col)             B[row] = ∑ xi^row yi
# where row, col = 0 to n, except [0,0]

A[0,0] = N
for row in range(n+1):

    for col in range(n+1):
        if row == 0 and col == 0: continue
        
        A[row,col] = sum(X**(row+col))

    B[row] = sum(X**row * Y)

a = linalg.solve(A, B)


print("The polynomial equation :")
print('y = %f' % a[0], end=' ')
for i in range(1, n+1):
    print('%+f x^%d' % (a[i], i), end=' ')
print()
