#!/usr/bin/env python3

# Script Name:               Pyhton lists
# Author:                    Gerald
# Date of latest revision:   6/8/2023
# Purpose:                   Python lists       
# Instructions:     
#Create a Python script that includes the following:

#Assign to a variable a list of ten string elements.
#Print the fourth element of the list.
# this would be like var()[3]
#Print the sixth through tenth element of the list.
# this would be [6-10]
#Change the value of the seventh element to “onion”.

#Declartion of varibles:

# Python was reading the below code as one just variable so print(Todo)[5] would print out a letter instead of an entry
#Todo = ("Clean " "Take out trash " "Shop " "Laundry " "Appointment " "Work " "Feedcat " "Lawn " "Exercise " "Hobbies")

# Every string needs to be in quotation marks and was getting an error because of it
#Todo = [Clean,  Takeouttrash, Shop,  Laundry,  Appointment,  Work,  Feedcat,  Lawn,  Exercise,  Hobbies]
Todo = ['Clean', 'Takeouttrash', 'Shop', 'Laundry', 'Appointment', 'Work', 'Feedcat', 'Lawn', 'Exercise', 'Hobbies']



#Declaration of functions:





#Main
print(Todo[3])

# This should be 6:10 
#print(Todo[6-10])
print(Todo[5:9])
print