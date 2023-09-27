"""
Chapter 5 Exercise 4: Rivers

Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

rivers = {"Amazon River": "South America",
          "Danube River": "Europe",
          "Colorado River": "USA",
          }

for x in rivers:
  print(x, "runs through", rivers[x]) #the x represents the dictionary's keys, and the rivers[x] is the dictionary's values
print("")
for x in rivers:
  print(x)
print("")
for x in rivers:
  print(rivers[x])