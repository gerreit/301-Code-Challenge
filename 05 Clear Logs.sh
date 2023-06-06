#!/bin/bash

# Script Name:               Clear logs
# Author:                    Gerald
# Date of latest revision:   6/5/2023
# Purpose:                   Clear logs
# Instructions:
#Print to the screen the file size of the log files before compression
# stat -c "%s" /var/log/syslog
# stat -c "%s" /var/log/wtmp
#Compress the contents of the log files listed below to a backup directory
#/var/log/syslog
#/var/log/wtmp
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# $(date +"%Y-%m-%d %H %M %S")
#Example: /var/log/backups/syslog-20220928081457.zip
#Clear the contents of the log file
#Print to screen the file size of the compressed file
#Compare the size of the compressed files to the size of the original log files

#Declaration of variables:
syslog=/var/log/syslog
wtmp=/var/log/wtmp
time=$(date +"-%Y%m%d%H%M%S")

#Declaration of functions:
#compressbackup{
 #   gzip $syslog
  #  gzip $wtmp
#}

#Main
mkdir backup
stat -c "%s" var/log/syslog
stat -c "%s" $syslog
stat -c "%s" $wtmp
gzip $ "./backup"
gzip $wtmp