#!/usr/bin/python3
# Script Name:                  Port Scanner tool - Todo
# Date of latest revision:      9/11/23
# Purpose:                      Port Scanner 

#Import Libraries 
import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value (e.g., 1 second)
timeout = 1
sockmod.settimeout(timeout)

# Collect a host IP from the user
hostip = input("Enter the host IP address: ")

# Collect a port number from the user, then convert it to an integer data type
portno = int(input("Enter the port number: "))

def portScanner(portno):
    try:
        # Use the 'connect' method to check if the port is open
        sockmod.connect((hostip, portno))
        print("Port open")
    except socket.timeout:
        print("Port closed (timeout)")
    except ConnectionRefusedError:
        print("Port closed (connection refused)")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sockmod.close()

portScanner(portno)
