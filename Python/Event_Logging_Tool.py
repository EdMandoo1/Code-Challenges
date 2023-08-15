#!/usr/bin/env python3
# Script Name:                  Event Logging Tool pt. 1
# Author:                       Eduardo Ayala
# Date of latest revision:      08/14/23
# Purpose:                      Log events for port scans

#Import Libraries
import sys
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a FileHandler to write log messages to a file
log_file = 'network_scanner.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Add the FileHandler to the logger
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

def scan_port(host, port):

# Scan a TCP port on a given host.
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
    
# Perform a port scan on the given host.
# Prints the status of each port and lists the open ports.

    open_ports = []

    logger.info(f"Scanning ports for host: {host}")

    for port in range(1, 65536):
        if scan_port(host, port):
            logger.info(f"Port {port} is open.")
            open_ports.append(port)

    if open_ports:
        logger.info("\nOpen ports:")
        logger.info(open_ports)
    else:
        logger.info("No open ports found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python network_scanner.py <host>")
        sys.exit(1)

    host = sys.argv[1]

    try:
        socket.inet_aton(host)
    except socket.error:
        logger.error("Invalid IP address format.")
        sys.exit(1)

    scan_host(host)
