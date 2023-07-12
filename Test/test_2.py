#!/usr/bin/env python3

import subprocess
import datetime
import time
import sys

def ping_host(ip_address):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip_address])
        return True
    except subprocess.CalledProcessError:
        return False

def main(ip_address):
    while True:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        status = ping_host(ip_address)
        if status:
            print(f'{timestamp} Network Active to {ip_address}')
        else:
            print(f'{timestamp} Network Inactive to {ip_address}')
        time.sleep(2)  # Wait for 2 seconds before sending the next ping

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide an IP address as an argument.')
        sys.exit(1)
    ip_address = sys.argv[1]
    main(ip_address)