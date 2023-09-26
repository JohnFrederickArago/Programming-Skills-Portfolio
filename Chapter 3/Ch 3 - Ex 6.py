"""
Chapter 3 Exercise 6: Shrinking Guest List

You just found out that your new dinner table won’t arrive in time for the 
dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a 
message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names 
remain in your list. Each time you pop a name from your list, print a message
to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them 
know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your 
program.    
"""
guests = ["Albert Einstein", "Thomas Edison", "Nikola Tesla"]
print("I invite you,", guests[0]+", to dinner")
print("I invite you,", guests[1]+", to dinner")
print("I invite you,", guests[2]+", to dinner\n")

print(guests[0], "couldn't make it to dinner")
print(guests[1], "couldn't make it to dinner")
print(guests[2], "couldn't make it to dinner\n")

guests2 = ["Ryan Reynolds", "Hugh Jackman", "Tony Stark"]
print("I invite you,", guests2[0]+", to dinner as replacement for", guests[0])
print("I invite you,", guests2[1]+", to dinner as replacement for", guests[1])
print("I invite you,", guests2[2]+", to dinner as replacement for", guests[2],"\n")

print("I can only invite two people for dinner")
print("I'm sorry", guests2.pop(1)+", but I can only invite two people for dinner") #pop() function is to remove a specific item from the list
print(guests2[0], "and", guests2[1], "are still invited for dinner\n") #after removing specific items, the number in the list now starts from 0 and ends with 1. Different from the previous list which is 0 to 2

del guests2[0] 
del guests2[0] #del function is used to remove the rest of the items in the list

print(guests2)

