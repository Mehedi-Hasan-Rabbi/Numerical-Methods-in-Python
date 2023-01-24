# https://github.com/michaelehab/Numerical-Methods

import numpy as np
import math

def f1(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

def simpson(start, end, n, f):
    h = float((end - start) / n)
    ans = f(start) + f(end)
    i = 0
    while(start + h != end):
        if i % 2 == 0 :
            ans += 4 * f(start + h)
        else:
            ans += 2 * f(start + h)
        start += h
        i += 1
    return ans * (h / 3)  

def test_simpson():
    """
    Example:
        F1(X) = 1 / (1 + x)
        Integration from 0 to 0.1 using 1 segment
        = 0.09531
    """
    print("Integrating F(x) using Simpson rule:")
    start = float(input("Enter the start point: "))
    end = float(input("Enter the end point: "))
    n = int(input("Enter the number of segments: "))
    ans = simpson(start, end, n, f1)
    print("The answer is {}".format(ans))

test_simpson()