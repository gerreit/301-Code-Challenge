#!/bin/bash

# Script Name:               Code 1 log directory
# Author:                    Gerald
# Date of latest revision:   5/31/2023
# Purpose:          Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename         

#Declaration of variables:


#Declaration of functions:


#Main
#due to an error on my devkit I use for these challenges I was unable to properly test this code
cp /var/log/syslog .
time=$(date +"%Y-%m-%d %T")

$time >> /var/log/syslog 

