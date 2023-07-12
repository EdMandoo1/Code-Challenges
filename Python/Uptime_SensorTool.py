#!/usr/bin/env python3

import subprocess
import datetime
import time

# Function takes an IP address and sends single ping packet to specified IP address. 
def ping_host(ip_address):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip_address])
        return True
    except subprocess.CalledProcessError:
        return False
# Main initializes IP address variable and 'while True' loop 
def main():
    ip_address = '8.8.8.8'  # Replace with the IP address you want to ping
    while True:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        status = ping_host(ip_address)
        if status:
            print(f'{timestamp} Network Active to {ip_address}')
        else:
            print(f'{timestamp} Network Inactive to {ip_address}')
        time.sleep(2)  # Wait for 2 seconds before sending the next ping

# The main function is executed if the script is run directly (i.e., not imported as a module) using if __name__ == '__main__':
if __name__ == '__main__':
    main()