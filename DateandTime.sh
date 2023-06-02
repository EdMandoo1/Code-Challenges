#!/bin/bash

# Script Name:                  Date and Time
# Author:                       Eduardo Ayala
# Date of latest revision:      05/31/2023
# Purpose:                      Append Date and Time

# cp /var/log/syslog 
current_date=$(date +"%Y-%m-%d_%H:%M:%S")
# Main

echo "$(date +"%Y-%m-%d-%H:%M:%S")"
# Append Date and Time to file
cp /var/log/syslog "syslog_$current_date" 
