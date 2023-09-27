"""
Chapter 5 Exercise 2: Glossary 

A Python dictionary can be used to model an actual dictionary. However, to avoid
confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use 
these words as the keys in your glossary, and store their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word 
followed by a colon and then its meaning, or print the word on one line and then print 
its meaning indented on a second line. Use the newline character (\n) to insert a blank 
line between each word-meaning pair in your output.  
"""

glossary = {"Arithmetic Operators": "are +, -, *, /, %",
            "Assignment Operators": "are +=, -=, *=, /=",
            "Relational Operators": "are <, >, <=, >=, ==, !=",
            "Logical Operators": "are and, or, not ",
            "Bitwise Operators": "are &, |, ^, ~"
          }
print("Arithmetic Operators: ", glossary["arithmetic_operators"])
print("\nAssignment Operators: ", glossary["assignment_operators"])
print("\nRelational Operators: ", glossary["relational_operators"])
print("\nLogical Operators: ", glossary["logical_operators"]) 
print("\nBitwise Operators: ", glossary["bitwise_operators"]) 