"""
Chapter 6 Exercise 5: No Pastrami

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
appears in the list at least three times. Add code near the beginning of your program 
to print a message saying the deli has run out of pastrami, and then use a while loop to 
remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami 
sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ["Pastrami", "Egg", "Pastrami", "Seafood", "Pastrami"]
finished_sandwiches = []

print("The deli has ran out of Pastrami Sandwiches!")

while "Pastrami" in sandwich_orders:
  deli = sandwich_orders.remove("Pastrami")

while sandwich_orders:
  print("\n")
  deli = sandwich_orders.pop(0) 
  print("I made your", deli)
  finished_sandwiches.append(deli)
  print(finished_sandwiches, "is beaing made!")

print("\nSandwiches that was made: ")

for sandwiches in finished_sandwiches:
  print("I made", sandwiches, "Sandwich")