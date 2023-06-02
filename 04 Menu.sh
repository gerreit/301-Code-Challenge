#!/bin/bash

# Script Name:               Menu script
# Author:                    Gerald
# Date of latest revision:   6/2/2023
# Purpose:                   elseif options for a menu
# Instructions:
#Create a bash script that launches a menu system with the following options:
#Hello world (prints “Hello world!” to the screen)
# echo "Hello World!"
#Ping self (pings this computer’s loopback address)
# echo "Press 1 for Ping loopback"
# ping 127.0.0.1
#IP info (print the network adapter information for this computer)
# echo "Press 2 toShow IP Info"
# sudo lshw -class network | grep IP
#Exit
# Echo "Press 3 to Exit"
# Read and if variable matchesup exit
#Next, the user input should be requested.
# Use Read Command
#The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
# Elseif 
#Use a loop to bring up the menu again after the request has been executed
# press 1-4 for each option

#Declaration of variables:
# User stored variable from read command
answer="y"


#Declaration of functions:


#Main


while [ "$answer" == "y" ]; do
    echo "Hello World!"
    echo "Press 1 for Ping loopback"
    echo "Press 2 toShow IP Info"
    # i originally accidently had the E in echo capitalized and the command wouldnt work
    echo "Press 3 to Exit"
    read input

    if [ "$input" -eq 1 ]; then
        ping 127.0.0.1 -c 5
     elif [ "$input" -eq 2 ]; then
        sudo lshw -class network
    elif [ "$input" -eq 3 ]; then
        exit 0
    else
        echo "Choose a number between 1-3"
    fi

    read -p "Do you want to continue (y/n)? " answer
done
# -p stands for print then prints out whatever is in "" 