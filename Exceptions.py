__author__ = 'eduardo.fano'

from fractions import Fraction


try:
    a=float (input("Enter a number"))

except ValueError:
    print("You entered an invalid number")


print("The number is:",a)