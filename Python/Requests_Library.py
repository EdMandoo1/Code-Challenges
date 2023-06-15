#!/usr/bin/env python3
# Script Name:                  Requests_Library
# Author:                       Eduardo Ayala
# Date of latest revision:      06/06/23
# Purpose:                      To evaluate how a web server responds to outside requests

import requests
import http.client

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP Method
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Validate the selected HTTP Method
valid_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
if http_method not in valid_methods:
    print("Invalid HTTP Method selected.")
    exit()

# Print the request details
print("Request to be sent:")
print(f"URL: {url}")
print(f"Method: {http_method}")

# Ask the user for confirmation
confirmation = input("Confirm the request (y/n): ")

# Send the request if confirmed
if confirmation.lower() == "y":
    response = requests.request(http_method, url)

    # Print response header information
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    # Print response content
    print("Response Content:")
    print(response.text)
else:
    print("Request canceled.")
