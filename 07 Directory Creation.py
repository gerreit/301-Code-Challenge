#!/usr/bin/env python3

# Script Name:               Directory Creation
# Author:                    Gerald
# Date of latest revision:   6/7/2023
# Purpose:                   User gives files and python takes you to file path       
# Instructions:     
#Script must ask the user for a file path and read a user input string into a variable.
# This will use the input() command. Next line will prompt you to type in something that used as s a variable
#Script must use the os.walk() function from the os library.
# import os --> os.walk(input)
#Script must enclose the os.walk() function within a python function that hands it the user input file path.


#Declartion of varibles:
path = input("Type in a file path")


#Declaration of functions:
def lookup ():
    import os
    os.walk(path)
    print(path)




#Main
lookup
