"""
Chapter 6 Exercise 4: Deli 

Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as 
I made your tuna sandwich. As each sandwich is made, move it to the list of finished 
sandwiches. After all the sandwiches have been made, print a message listing each 
sandwich that was made.
"""

sandwich_orders = ["Egg", "Seafood", "Grilled Cheese"]
finished_sandwiches = []

while sandwich_orders:
  deli = sandwich_orders.pop(0) #.pop() to take out the value
  print("I made your", deli, "Sandwich")
  finished_sandwiches.append(deli) #.append() to place the value I took out from sandwich_orders to the finished_sandwiches list
  print(finished_sandwiches, "Sandwich is being made!\n")

print("Sandwiches that was made: ")

for sandwiches in finished_sandwiches: #for loop lists all items in the finished_sandwiches
  print("I made", sandwiches, "Sandwich")