import numpy as np
import math

def f3(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

def trapezoidal(start, end, n, f):
    h = float((end - start) / n)
    ans = f(start) + f(end)
    while(start + h != end):
        ans += 2 * f(start + h)
        start += h
    return ans * (h / 2)

def test_trapezoidal():
    print("Integrating F(x) using Trapezoidal rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of point within start and end: "))
    ans = trapezoidal(start, end, n, f3)
    print("The answer is {}".format(ans))

test_trapezoidal()