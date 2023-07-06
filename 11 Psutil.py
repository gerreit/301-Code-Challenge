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
cpu_times = psutil.cpu_times()
user_time = cpu_times.user
kernel = cpu_times.system
idle = cpu_times.idle
priority = cpu_times.nice
io = cpu_times.iowait
irq = cpu_times.irq
softirq = cpu_times.softirq
steal = cpu_times.steal
guest = cpu_times.guest

#Declaration of functions:

#Main

import psutil

print("Time in seconds spent by normal processes executing in user mode:", cpu_times)

print("Time in seconds spent by processes executing in kernel mode:", kernel)

print("Time in seconds when system was idle:", idle)

print("Time spent by priority processes executing in user mode:", priority)

print("Time spent waiting for I/O to complete:", io)

print("Time spent for servicing hardware interrupts:", irq)

print("Time spent for servicing software interrupts:", softirq)

print("Time spent by other operating systems running in a virtualized environment:", steal)

print("Time spent running a virtual CPU for guest operating systems:", guest)
