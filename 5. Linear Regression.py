
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
print()


# X = [3, 4, 5, 6, 7, 8]
# Y = [0, 7, 17, 26, 35, 45]

N = len(X)  # Number of data points

# ~~~~~~~~~~~~~~~~~~~~~~~~ Method 1: Using for loop ~~~~~~~~~~~~~~~~~~~~~~~~

sumx = sumy = sumx2 = sumxy = 0 # Initial value of summation variables
for i in range(N):
    sumx += X[i]
    sumy += Y[i]
    sumx2 += X[i]**2
    sumxy += X[i]*Y[i]
meanx = sumx / N
meany = sumy / N

a1 = (N*sumxy - sumx*sumy) / (N*sumx2 - sumx**2)
a0 = meany - a1 * meanx

# ~~~~~~~~~~~~~~~~~ Method 2: Using numpy array, sum, mean ~~~~~~~~~~~~~~~~~

from numpy import array, mean

# sum(X**2) requires X to be a numpy array as python list cannot be squared
X = array(X, float)

a1 = (N*sum(X*Y) - sum(X)*sum(Y)) / (N*sum(X**2) - sum(X)**2)
a0 = mean(Y) - a1 * mean(X)


print("The straight line equation :")
s = "-" if a1<0 else "+"
a1 = -a1 if a1<0 else a1
print('y = %.3f %s %.3f x' %(a0, s, a1))
