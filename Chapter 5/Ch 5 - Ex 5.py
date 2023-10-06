"""
Chapter 5 Exercise 5: Pets

Make several dictionaries, where each dictionary represents a different pet. In each 
dictionary, include the kind of animal and the owner’s name. Store these dictionaries 
in a list called pets. Next, loop through your list and as you do, print everything you 
know about each pet
"""

Daisy = {"Name": "Daisy",
         "Breed": "Chihuahua",
         "Owner": "Wacky"
         }
Buddy = {"Name": "Daisy",
         "Breed": "Golden Retriever",
         "Owner": "Bokal"
         }
Coco = {"Name": "Daisy",
        "Breed": "Dachshund",
        "Owner": "President"
        }
list_of_pets = [Daisy, Buddy, Coco] #stored all dictionaries in a list

for x in list_of_pets:
  print(list_of_pets[x]) #printed each of the items in the list