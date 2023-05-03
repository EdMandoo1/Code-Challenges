#!/bin/bash

# Script Name:                  Bash Conditional Statement
# Author:                       Eduardo Ayala
# Date of latest revision:      05/01/2023
# Purpose:                      To detect a file

# Declaration of variables
Heros=("SilverSurfer" "Hulk" "Thor")
#Main
for Hero in "${Heros[@]}"
do
#Here is my Loop
   if [[ "$Hero" == "SilverSurfer" ]]; then
    echo "$Hero is the strongest!"
   else 
    echo "$Hero? I think not!"
   fi
done
