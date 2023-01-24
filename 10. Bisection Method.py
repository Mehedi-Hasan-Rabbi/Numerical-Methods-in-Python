import math

def f(x):
    red = (x*math.pi) / 180          # Converting degree to radian
    return 3*x - math.cos(red) - 1   # sin, cos, tan takes redian value so convert degree to radian

a, b = input("Enter two interval a and b: ").split()
a = float(a)
b = float(b)

if f(a)*f(b) > 0:
    print("No roots exist within the given interval")
    raise SystemExit()

if f(a)*f(b) == 0:
    if f(a) == 0:
        print("The root is: %0.5f" %a)
    if f(b) == 0:
        print("The root is: %0.5f" %b)
    raise SystemExit()

root = a
while abs(f(root)) >= 1e-6:
    root = (a+b)/2

    if f(a) * f(root) < 0:
        b = root
    elif f(a) * f(root) > 0:
        a = root
    else:
        break


print("The root is: %0.5f" %root)