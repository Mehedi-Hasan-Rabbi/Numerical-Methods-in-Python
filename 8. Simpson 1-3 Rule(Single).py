def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

print("Single Application Trapezoidal Rule:")
a = float(input("Enter starting value: "))
b = float(input("Enter ending value: "))
e = float(input("Enter exact value: "))

I = ((b-a)*(f(a)+ (4*f((b-a)/2)) +f(b)))/6.0

print("\nIntegral of the equation: %f" %I)

error = abs(e-I)
print("The error: ", error)

print("Percentage: ", (error*100)/e, "%")

