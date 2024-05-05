#!/usr/bin/env python3
# Script Name:                  Extract and Convert Trailing number
# Author:                       Eduardo Ayala
# Date of latest revision:      05/04/24
# Purpose:                      o find and convert the last number in a string into a floating point number.

msg = "The final countdown 858"

# Find the last space in the string
last_space_index = msg.rfind(' ')

# Extract the substring from after this space to the end
number_str = msg[last_space_index + 1:]

# Convert the substring to a float
number = float(number_str)

# Print the floating point number
print(number)
