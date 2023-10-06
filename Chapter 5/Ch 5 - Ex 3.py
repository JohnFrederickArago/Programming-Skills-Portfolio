"""
Chapter 5 Exercise 3: Glossary 2 

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
(page 99) by replacing your series of print() calls with a loop that runs through the 
dictionary’s keys and values. When you’re sure that your loop works, add five more 
Python terms to your glossary. When you run your program again, these new words and 
meanings should automatically be included in the output.
"""

glossary = {"Arithmetic Operators": "are +, -, *, /, %",
            "Assignment Operators": "are +=, -=, *=, /=",
            "Relational Operators": "are <, >, <=, >=, ==, !=",
            "Logical Operators": "are and, or, not ",
            "Bitwise Operators": "are &, |, ^, ~",
            "String": "is a sequence of characters",
            "Integer": "is a whole number",
            "Float": "is a decimal number",
            "Boolean": "is True/False",
            "While loop": "is a type of loop that doesn't stop unless given condition is met"
          } #added five more keys and values
for x in glossary: #used for loop to loop through the dictionary
  print(x, "-", glossary[x]) #the x represents the dictionary's keys, and the glossary[x] is the dictionary's values