"""
Chapter 4 Exercise 2: Alien Colors #2 

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 
points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 
10 points.

•Write one version of this program that runs the if block and another that runs 
the else block.
"""

alien_color = input("You shot an alien: ")
if alien_color=="green": #if true, the if block executes
    print("You shot a green alien!")
    print("You earn 5 points!")
else: #else the else block will execute
    print("You shot a non-green alien!")
    print("You earn 10 points!")