# Author: Mehedi Hasan
from numpy import array, linalg

N = int(input("Enter number of equation: "))
co_eff = []
const = []

for i in range(N):
    row = []
    for j in range(N):
        x = float(input("Enter coefficient " + str(j+1) + " of equation " + str(i+1) + ": "))
        row.append(x)
    co_eff.append(row)
    c = float(input("Enter constent of quation " + str(i+1) + ": "))
    const.append(c)

A = array(co_eff)
B = array(const)

print("\nCo-efficient's of equation: ")
print(A)
print("\nCo-efficient's of equation: ")
print(B)

det_matrix = linalg.det(A)

if abs(det_matrix) < 1e-12:
    print("Two or more equation are coincident or parallel\n")
    raise SystemExit

Dx_matrix = []
for i in range(N):
    temp = A.copy()                            # Making a copy to keep A unchanged
    temp[:, i] = B                             # Replace i th coloumn of C with B

    Dx = linalg.det(temp)
    Dx_matrix.append(Dx)


Solution = Dx_matrix/det_matrix

print("\nSolution is:")
print(Solution)
