"""
Chapter 6 Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until 
they enter a 'quit' value. As they enter each topping, print a message saying you’ll 
add that topping to their pizza.
"""

while True: #while the condition is true, the while block executes
  toppings = input("Enter your toppings 'quit' to finish: ") #user input for toppings
  if toppings.lower()=="quit": #if the user type 'quit'
    break #break to stop the loop
  print("Added", toppings, "to your pizza!")

confirm = input("Are you sure? (Yes/No): ") #user input to ask the user if he is sure he wants to quit

while True:
  if confirm.lower()=="no": #if the user type 'no', the loop will continue to work
    toppings = input("Enter your toppings 'quit' to finish: ") 
    if toppings.lower()=="quit": #if the user once again types 'quit', the loop will end
      print("Your pizza is being prepared!")
      break
  if confirm.lower()=="yes": #if the user, instead of typing 'no', types 'yes'; the loop will then end
    print("Your pizza is being prepared!")
    break
  print("Added", toppings, "to your pizza!")

print("Your pizza is served!") 
print("Thank you for coming!") #prints at the end of the code