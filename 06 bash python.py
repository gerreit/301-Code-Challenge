#!/usr/bin/env python3

# Script Name:               Bash in Python
# Author:                    Gerald
# Date of latest revision:   6/6/2023
# Purpose:                   run bash commands in python
# Instructions:
#The Python module “os” must be utilized
#At least three variables must be declared and referenced in Python
#The Python function print() must be used at least three times
#Include execution of the following bash commands inside your Python script:

#use these commands
#whoami
#ip a
#lshw -short

#Declartion of varibles:
# to call this variable do put the defined variable word in () like this (variable)
variable = "this is variable stuff"
user = os.system("whoami")
IP =("ip -a")
show = ("lshw -short")

#Declaration of functions:


#Main

print("this is text") 
print(variable)


print("This script will do the following")
print("Show IP information")
print("Show the name of the current user")
print("Show system hardware information")

import os
os.system(IP)
os.system(user)
os.system(show)