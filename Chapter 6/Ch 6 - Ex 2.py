"""
Chapter 6 Exercise 2: Movie Tickets:

A movie theater charges different ticket prices depending on a person’s age. If a 
person is under the age of 3, the ticket is free; if they are between 3 and 12, the 
ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which 
you ask users their age, and then tell them the cost of their movie ticket
"""

while True:
  age = int(input("Enter your age: ")) #user enters their age
  if age<3: #if age less than 3
    print("Your ticket is free!")
  elif age>=3 and age<=12: #if age more than or equal to 3 and if age more than or equal to 12
    print("Your ticket is $10")
  else: #else above 12 years old get $15 ticket
    print("Your ticket is $15")
  done = input("is that all? (yes/no): ") #confirmation if the user is done
  if done.lower()=="yes": #if they type 'yes', the loop breaks
    print("Thank you for purchasing tickets!")
    break
  if done.lower()=="no": #if they type 'no', the loop continues
    continue