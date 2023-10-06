"""
Chapter 7 Exercise 4: Large Shirts 

Modify the make_shirt() function so that shirts are large by default with a message 
that reads I love Python. Make a large shirt and a medium shirt with the default 
message, and a shirt of any size with a different message.
"""

def make_shirt(size="Large", text="I love Python"):
  print("The size of the shirt:", size)
  print("The text of the shirt:", text)

make_shirt() #called the function by value

print()

make_shirt(size="Medium") #changed the size parameter to Medium 

print()

make_shirt(size="Small", text="I am in  love with Python") #changed the size and text of the parameter