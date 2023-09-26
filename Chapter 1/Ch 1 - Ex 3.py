"""
Chapter 1 - Exercise 3 : Print date and Time

Write a Python program to display the current date and time.
"""

import datetime 
time = datetime.datetime.now() 
print("Current date and time: ")
print(time.strftime("%Y-%m-%d %H:%M:%S \n\n"))