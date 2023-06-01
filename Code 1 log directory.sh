#!/bin/bash

# Script Name:               Code 1 log directory
# Author:                    Gerald
# Date of latest revision:   5/31/2023
# Purpose:          Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename         

#Declaration of variables:


#Declaration of functions:


#Main
cp /var/log/syslog .
time=$(date +"%Y-%m-%d %T")

echo $time >> /var/log/syslog 

