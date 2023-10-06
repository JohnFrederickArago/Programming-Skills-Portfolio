"""
Chapter 2 - Exercise 5: USB Shopper

A girl heads to a computer shop to buy some USB sticks. She loves USB 
sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how
many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

a = 50 
b = 6
c = int(a/b) #division arithmetic operator to divide variables a and b
print("The girl can get", c, "pieces of USB sticks\n") #print variable c

d = int(b*c) #multiply the value of b and c
e = int(a-d) #subtract the value of a and d
print("The girl will have £", e, "left") #print variable e
