#!/bin/bash

# Script Name:               Permissions script
# Author:                    Gerald
# Date of latest revision:   6/1/2023
# Purpose:                   Changes permissions on file
#Prompts user for input directory path.
# echo Put in your file path
# Use a read command
# read path which will be user input stored as a variable

#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Echo What input permissions number would you like maybe like 744 so creat gets full rights but everyone else can see
# Read command again 
# User input stored as perm variable

#Navigates to the directory input by the user and changes all files inside it to the input setting.
# $path
# $perm

#Prints to the screen the directory contents and the new permissions settings of everything in the directory.       
# echo and whatever that command is going to be i gotta look that up

#Declaration of variables:


#Declaration of functions:


#Main
mkdir Test 
cd Test
touch test.txt
echo "Input a file path you want to change permissions for? Inputing ./Test/test.txt will use the Test folder and file generated for this script"
read path
echo
echo "What permissions number would you like to give to this folder? 700 only gives creator permissions"
read perm
echo
cd $path
chmod $perm 
