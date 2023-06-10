#!/usr/bin/env python3

# Script Name:               Conditional Statements
# Author:                    Gerald
# Date of latest revision:   6/9/2023
# Purpose:                   Conditional Statemetns   
# Instructions:     
#Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b



#Declartion of varibles:
#  prints the text pick a number, then after the comma which divides commands stores input as variable number
#number = ("Pick a number: ")

number = input("Enter a number: ")
print(number)


#Declaration of functions:





#Main
# if this isnt a string like in "" it will always come back as not equal to 6
#if number == "6":
    #print("Equal to 6")
    #if number < "6":
        

if number == 6:
    print("Your number is equal to 6")
elif number != 6:
    print("Your number is not equal to 6")
elif number < 6:
    print("Your number is less than 6")
elif number <= 6:
    print("Your number is less than or equal to 6")
elif number > 6:
    print("Your number is greater than 6")
elif number >= 6:
    print("Your number is greater than or equal to 6")
else:
    print("Error")
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

#print("Your name is", name)
#print("Your age is", age)