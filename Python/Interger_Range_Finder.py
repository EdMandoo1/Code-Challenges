#!/usr/bin/env python3
# Script Name:                  Integer Ranger Finder 
# Author:                       Eduardo Ayala
# Date of latest revision:      04/28/24
# Purpose:                      Determine the range of integer inputs

def get_numbers():
    largest = None
    smallest = None

    while True:
        num_input = input("Enter a number: ")
        if num_input == "done":
            break

        try:
            num = int(num_input)
            if largest is None or num > largest:
                largest = num
            if smallest is None or num < smallest:
                smallest = num
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'done' to finish.")
    
    print("Maximum is", largest)
    print("Minimum is", smallest)

get_numbers()
