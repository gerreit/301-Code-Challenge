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

status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}


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
confirmation = input("Do you want to proceed? (Y/N): ")
if confirmation.lower() != "y":
    exit()
# pass is a command to skip a elif segment 
if person == "1":
    response = requests.get(site)
elif person == "2":
    response = requests.post(site)
elif person == "3":
    response = requests.put(site)
elif person == "4":
    response = requests.delete(site)
elif person == "5":
    response = requests.head(site)
elif person == "6":
    response = requests.patch(site)
elif person == "7":
    response = requests.options(site)
else:
    print("Pick a number 1-7")
