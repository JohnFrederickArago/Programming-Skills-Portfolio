"""
Chapter 7 Exercise 2: Favorite Book

Write a function called favorite_book() that accepts one parameter, title. The function 
should print a message, such as One of my favorite books is Alice in Wonderland. Call 
the function, making sure to include a book title as an argument in the function call.
"""

def favorite_book(title): #title as the parameter
  print("One of my favourite book is", title)

favorite_book("Ikigai") #calling the funciton by value
favorite_book("Goosebumps")
favorite_book("Harry Potter")