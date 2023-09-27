"""
Chapter 4 Exercise 5: Favorite Fruit

Make a list of your favorite fruits, and then write a series of independent 
if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit 
is in your list. If the fruit is in your list, the if block
should print a statement,such as You really like bananas!
"""

favorite_fruits = ["Mango", "Orange", "Watermelon"]
if "Mango" in favorite_fruits: #Mango in list = True
    print("You really like Mango")
if "Banana" in favorite_fruits: #Banana in list = False
    print("You don't like Banana")
if "Orange" in favorite_fruits: #Orange in list = True
    print("You really like Orange") 
if "Apple" in favorite_fruits: #Apple in list = False
    print("You don't like Apple")
if "Watermelon" in favorite_fruits: #Watermelon in list = True
    print("You really like Watermelon") 