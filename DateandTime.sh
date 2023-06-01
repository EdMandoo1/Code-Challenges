#!/bin/bash

# Script Name:                  Date and Time
# Author:                       Eduardo Ayala
# Date of latest revision:      05/31/2023
# Purpose:                      Append Date and Time

# Copies /var/log/syslog to the current working directory
# Appends the current date and time to the filename

# Declaration of variables
current_date=$(date +"%Y-%m-%d-%H:%M:%S")

# Main
echo "$(date +"%Y-%m-%d-%H:%M:%S")

# Append Date and Time to file
cp /var/log/syslog "~/syslog_${current_date}" 

