"""
Chapter 4 Exercise 3: Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for 
the appropriate color alien.
"""

alien_color = input("You shot an alien: ")
if alien_color=="green": #if green=green, it is true
    print("You shot a green alien!")
    print("You earn 5 points!")
elif alien_color=="yellow": #if yellow=yellow, it is true
    print("You shot a yellow alien!")
    print("You earn 10 points!")
elif alien_color=="red": #if red=red, it is true
    print("You shot a red alien!")
    print("You earn 15 points!")
else:
    print("You shot nobody!")
    print("You earn 0 point!")
