from math import *

print("This is a quadratic equation calculator. If the quadratic equation is:")
print("Ax^2 + Bx + C = 0")
print("enter the following:")

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

D = B**2 - (4*A*C)

if (D >= 0):
    x1 = (-B + sqrt(D))/(2*A)
    x2 = (-B - sqrt(D))/(2*A)
    print("Your values are {0:0.2f} or {1:0.2f}.".format(x1,x2))
else:
    print("Your values are")
    print("( -{0:0.2f} +/- {1:0.2f}i ) / {2:0.2f}".format(B,sqrt(-D),2*A))
