def dy(x):
    return -(2*x**3) + (12*x**2) - (20*x) + 8.5

def f(x):
    return -(0.5*x**4) + (4*x**3) - (10*x**2) + (8.5*x) + 1


x = float(input("Enter starting point (x0): "))
xn = float(input("Enter ending point (xn): "))
y = float(input("Enter initial condition (y): "))
h = float(input("Enter step size (h): "))

n = int((xn-x)/h)

print("x \t\ty(Euler) \ty(Analytical)")
print("%f \t%f \t%f" %(x, y, f(x)))

for i in range(n):
    y = y + dy(x) * h
    x = x + h

    print("%f \t%f \t%f" %(x, y, f(x)))