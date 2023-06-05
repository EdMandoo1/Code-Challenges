#!/bin/bash

# Script Name:                  Conditionals in Menu Systems   
# Author:                       Eduardo Ayala
# Date of latest revision:      06/01/2023
# Purpose:  

print_menu() {
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    echo -n "Please enter your choice: "
}
hello_world() {
    echo "Hello world!"
}

ping_self() {
    ping -c 4 127.0.0.1
}

ip_info() {
    ip -c a
}

while true; do 
print_menu
read -r choice

if [[ $choice == 1 ]]; then 
hello_world
elif [[ $choice == 2 ]]; then
ping_self
elif [[ $choice == 3 ]]; then 
ip_info
elif [[ $choice == 4 ]]; then 
echo "Exiting..."
break
else 
echo "Invalid choice. Please try again. " 
fi 
echo 
done
