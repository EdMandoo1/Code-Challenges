#!/usr/bin/env python3
# Script Name:                  Conditional else elif
# Author:                       Eduardo Ayala
# Date of latest revision:      06/06/23
# Purpose:                      Script using "if" statements

import os

a = 5
b = 10

if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
    if a < b:
        print("a is less than b")
    elif a <= b:
        print("a is less than or equal to b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is greater than or equal to b")
else:
    print("This condition is not possible to reach")