"""
Chapter 2 - Exercise 3: Stripping Names 

Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some 
whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, “\t” and “\n”, 
at least once.

Print the name once, so the whitespace around the name is 
displayed.

Then print the name using each of the three stripping functions, 
lstrip(), rstrip(), and strip().
"""

a = "\n\tFrederick\t\n"

print(a)
print(a.lstrip("\t\n")) #lstrip to remove whitespace characters on the left side of the name
print(a.rstrip("\t\n")) #rstrip tp remove whitespace characters on the right side of the name
print(a.strip("\t\n")) #strip to remove all whitespace characters before and after the name