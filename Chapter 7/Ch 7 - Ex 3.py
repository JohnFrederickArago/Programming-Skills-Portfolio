"""
Chapter 7 Exercise 3: T-Shirt

Write a function called make_shirt() that accepts a size and the text of a message that 
should be printed on the shirt. The function should print a sentence summarizing the size 
of the shirt and the message printed on it. Call the function once using positional 
arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size, text):
  print("The size of the shirt:", size)
  print("The text of the shirt:", text)

size1 = input("Enter the size: ")
text1 = input("Enter the text: ")
make_shirt(size1, text1) #called the function by reference 

print()

make_shirt("Small", "Hello World") #called the function by value

print()

make_shirt(size="Extra Large", text="Hello World") #called the function using keyword arguments