"""
Chapter 1 - Exercise 5: Compute area of Circle

Write a Python program which accepts the radius of a circle from the 
user and compute the area.
"""

from math import pi #imported math to get pi 
r = int(input("Enter the radius of the Circle: ")) #integer user input
print("The Area of the Circle is: ", (pi*r**2)) #print the formula to get the area of the circle with arithmetic operators and the pi from the math library