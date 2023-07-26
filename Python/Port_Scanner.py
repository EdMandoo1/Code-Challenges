#!/usr/bin/env python3
# Script Name:                  Port Scanning
# Author:                       Eduardo Ayala
# Date of latest revision:      07/25/23
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed

# Import libraries
import sys
from scapy.all import *

# Define functions 
def tcp_port_scanner(host, port_range):
    open_ports = []
    closed_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        response = sr1(IP(dst=host) / TCP(dport=port, flags="S"), timeout=1, verbose=False)

        if response is None:
            closed_ports.append(port)
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            open_ports.append(port)
            send(IP(dst=host) / TCP(dport=port, flags="AR"), verbose=False)
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            closed_ports.append(port)
        else:
            print(f"Port {port} is filtered and silently dropped.")

    return open_ports, closed_ports

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

# Putting a range limit on the port search
    if start_port > end_port or start_port < 1 or end_port > 65535:
        print("Invalid port range.")
        sys.exit(1)

    open_ports, closed_ports = tcp_port_scanner(host, (start_port, end_port))

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open.")

    if closed_ports:
        print("Closed ports:")
        for port in closed_ports:
            print(f"Port {port} is closed.")