#!/usr/bin/env python3
# Script Name:                  Network Scanning
# Author:                       Eduardo Ayala
# Date of latest revision:      07/27/23
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed

# Import libraries
import sys
import socket

def scan_port(host, port):
    
    # Function to scan a TCP port on a given host.
    # Returns True if the port is open, False otherwise.
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))

            if result == 0:
                return True
            else:
                return False
    except socket.error:
        return False

def scan_host(host):
    
    # Function to perform a port scan on the given host.
    # Prints the status of each port and lists the open ports.
    
    open_ports = []

    print(f"Scanning ports for host: {host}")

# Can use range(1,1025) to scan only well-known ports
# Below scans ALL ports
    for port in range(1, 65536):
        if scan_port(host, port):
            print(f"Port {port} is open.")
            open_ports.append(port)

    if open_ports:
        print("\nOpen ports:")
        print(open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_scanner.py <host>")
        sys.exit(1)

    host = sys.argv[1]

# Check if the provided host is a valid IP address.
    try:
        socket.inet_aton(host)  
    except socket.error:
        print("Invalid IP address format.")
        sys.exit(1)

    scan_host(host)
