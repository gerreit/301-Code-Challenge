#!/usr/bin/env python3

# Script Name:               File Handling
# Author:                    Gerald
# Date of latest revision:   6/12/2023
# Purpose:                   Creates a text file, edits line, then deletes    
# Instructions:     
#Using file handling commands 
#create a Python script that creates a new .txt file 
#appends three lines 
#prints to the screen the first line
#then deletes the .txt file.


#Declartion of varibles:
words = open("Ops10text", "w")
line1 = words.readlines(1)

#Declaration of functions:
#words is the variable name, write is the command of what we're doing in this case writing text
# The "" containts the text and tells python that thats a string, while the \n is to start a new line




#Main
# This writes the text in "" in the files
words.write("Example text\n")
words.write("This is a second line of text\n")
words.write("A final line of text\n")
#then you have to close the file since you cant just switch to read
words.close
#open up the file in read mode the "r" denotes read mode
words = open("Ops10text", "r")
# I dont know why below doesnt work, not even when I switch it to 1
#words.readlines(0)
#Chat GPT saids to make it a variable first and I dont understand why
#lines = words.readlines()

# Print the first line
line1 = lines[0]
print(line1)
words.close
#The Code below deletes the fiel
import os 
os.remove(Ops10text)