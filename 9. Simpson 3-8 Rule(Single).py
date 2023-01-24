def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

print("Single Application Trapezoidal Rule:")
a = float(input("Enter starting value: "))
b = float(input("Enter ending value: "))
e = float(input("Enter exact value: "))

h = (b-a)/3

I = ((b-a)*(f(a)+ 3*(f(a+h)+f(a+h+h)) +f(b)))/8.0

print("\nIntegral of the equation: %f" %I)

error = abs(e-I)
print("The error: ", error)

print("Percentage: ", (error*100)/e, "%")

