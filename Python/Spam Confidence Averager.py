#!/usr/bin/env python3
# Script Name:                  Requests_Library
# Author:                       Eduardo Ayala
# Date of latest revision:      06/06/23
# Purpose:  to read a file, find lines with "X-DSPAM-Confidence:", extract the confidence values, and calculate their average.

# Prompt for the file name
file_name = input("Enter file name: ")

try:
    # Open the file
    with open(file_name, 'r') as file:
        count = 0
        total = 0.0
        
        # Read through the file line by line
        for line in file:
            # Look for lines that start with 'X-DSPAM-Confidence:'
            if line.startswith("X-DSPAM-Confidence:"):
                count += 1
                # Extract the floating point value from the line
                confidence = float(line.strip().split(":")[1])
                total += confidence
        
        # Compute the average
        if count > 0:
            average = total / count
            # Produce the output
            print(f"Average spam confidence: {average}")
        else:
            print("No lines with 'X-DSPAM-Confidence:' found.")

except FileNotFoundError:
    print(f"File not found: {file_name}")
