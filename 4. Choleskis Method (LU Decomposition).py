from numpy import array, zeros, sqrt

def decomposition(A):
    N = len(A)
    L = zeros((N,N))
    U = zeros((N,N))

    for j in range(N):                                  # j = 0 to N-1

        # Upper Triangular
        for i in range(j+1):                            # i = 0 to j
            
            U[i,j] = A[i,j] - sum(U[:i,j] * L[i,:i])    # k = 0 to i-1

        # Lower Triangular
        L[j,j] = 1                                          # i = j, Diagonal 1

        for i in range(j+1, N):                             # i = j+1 to N-1

            L[i,j] = (A[i,j] - sum(U[:j,j]*L[i,:j]))/U[j,j] # k = 0 to j-1

    print('LU Decomposition:')
    print('[L] =\n', L, sep='')
    print('[U] =\n', U, sep='', end='\n\n')
    return L, U


def solveLU(A, B):
    L, U = decomposition(A)
    N = len(L)
    
    X = zeros(N)
    Y = zeros(N)

    # Forward Substitution
    for i in range(N):                                      # i = 0 to N-1
        Y[i] = (B[i] - sum(L[i,:i] * Y[:i]))                # j = 0 to i-1

        # sumj = 0
        # for j in range(i):
        #     sumj += L[i,j] * Y[j]
        # Y[i] = (B[i] - sumj)

    # Backward Substitution
    for i in range(N-1, -1, -1):                            # i = N-1 to 0
        X[i] = (Y[i] - sum(U[i,i+1:] * X[i+1:])) / U[i,i]   # j = i+1 to N-1

        # sumj = 0
        # for j in range(i+1, N):
        #     sumj += U[i,j] * X[j]
        # X[i] = (Y[i] - sumj) / U[i,i]

    return X


# System of Equations

A = array([[1,1,-1],
           [2,3,5],
           [3,2,-3]], float)
B = array([2,-3,6], float)



N = len(A)


X = solveLU(A, B)

print("The Solution of the System:")
for i in range(N):
    print('X[', i+1, '] = ', round(X[i], 6), sep='')

