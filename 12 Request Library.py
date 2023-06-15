#!/usr/bin/env python3

# Script Name:               Request Library
# Author:                    Gerald
# Date of latest revision:   6/14/2023
# Purpose:                    
# Instructions:     
# Prompt the user to type a string input as the variable for your destination URL.

#Prompt the user to select a HTTP Method of the following options:
#GET
#POST
#PUT
#DELETE
#HEAD
#PATCH
#OPTIONS


#Declartion of varibles:
import requests
site = input("Enter a site url: ")
#number = input("Enter a number: ")
request = requests.get(site)
post = requests.post(site)
put = requests.put(site)
delete = requests.delete(site)
head = requests.head(site)
patch = requests.patch(site)
options = requests.options(site)



# https://api.github.com

#Declaration of functions:




#Main
print("Press 1 for HTTP Get")
print("Press 2 for HTTP Post")
print("Press 3 for HTTP Put")
print("Press 4 for HTTP Delete")
print("Press 5 for HTTP Head")
print("Press 6 for HTTP Patch")
print("Press 7 for HTTP Options")
person = input()
# pass is a command to skip a elif segment 
if person == "1":
    print(request)
elif person == "2":
    print(post)
elif person == "3":
    print(put)
elif person == "4":
    print(delete)
elif person == "5":
    print(head)
elif person == "6":
    print(patch)
elif person == "7":
    print(options)


#import requests

#request(print)
#Put this all in an if loop

print(request)