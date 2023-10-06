"""
Chapter 3 Exercise 5: Change Guest List 

You just heard that one of your guests can’t make the dinner, so you need to 
send out a new set of invitations. You’ll have to think of someone else to 
invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of 
your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the 
name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still 
in your list.
"""

guests = ["Albert Einstein", "Thomas Edison", "Nikola Tesla"]
print("I invite you,", guests[0]+", to dinner") #combination of comma and plus sign to insert my list
print("I invite you,", guests[1]+", to dinner")
print("I invite you,", guests[2]+", to dinner\n") #\n to have a line space in between invitations

print(guests[0], "couldn't make it to dinner")
print(guests[1], "couldn't make it to dinner")
print(guests[2], "couldn't make it to dinner\n")

guests2 = ["Ryan Reynolds", "Hugh Jackman", "Tony Stark"]
print("I invite you,", guests2[0]+", to dinner as replacement for", guests[0])
print("I invite you,", guests2[1]+", to dinner as replacement for", guests[1])
print("I invite you,", guests2[2]+", to dinner as replacement for", guests[2])