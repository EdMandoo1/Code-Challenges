#!/usr/bin/env python3
# the shebang line instructs the system to use the env command to locate the python3 interpreter and execute the script with it
# Script Name:                  Bash in Python
# Author:                       Eduardo Ayala
# Date of latest revision:      06/06/23
# Purpose:                      Linux commands within Python script

import os

# you can use os.system to execute the Bash command
os.system("ls")

# Assigned Variables
ip = os.system("ip -c a")
user = os.system("whoami")
specs = os.system("lshw -short")

# Printing listed variables
print(ip)
print(user)
print(specs)

