#!/usr/bin/env python3

# Script Name:               PSutil
# Author:                    Gerald
# Date of latest revision:   6/13/2023
# Purpose:                   Uses PSutil to do a variety of functions   
# Instructions:     
#Create a Python script that fetches this information using Psutil:

#Time spent by normal processes executing in user mode
#Time spent by processes executing in kernel mode
#Time when system was idle
#Time spent by priority processes executing in user mode
#Time spent waiting for I/O to complete.
#Time spent for servicing hardware interrupts
#Time spent for servicing software interrupts
#Time spent by other operating systems running in a virtualized environment
#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

#Declartion of varibles:


#Declaration of functions:




#Main


import Psutil
print(psutil.cpu_times())
print()