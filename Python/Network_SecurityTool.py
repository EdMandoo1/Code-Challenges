#!/usr/bin/env python3
# Script Name:                  Network Security Tool
# Author:                       Eduardo Ayala
# Date of latest revision:      07/26/23
# Purpose:                      TCP Port Range Scanner that tests whether a TCP port is open or closed

# Import libraries
import sys
import socket
from scapy.all import *

# Replace <host>:<start_port>-<end_port> with the target host and the port range to scan, and <network_address>/<CIDR_block> with the network address and CIDR block to perform the ICMP Ping Sweep. 

def scan_port(host, port):
    
    #Function to scan a TCP port on a given host.
    #Returns "open" if the port is open, "closed" if the port is closed, or "filtered" if the port is filtered.
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))

            if result == 0:
                return "open"
            elif result == 111:
                return "closed"
            else:
                return "filtered"
    except socket.error:
        return "error"

def tcp_port_scanner(host, port_range):
    #Function to perform a TCP Port Range Scanner on the given host and port range.
   
    open_ports = []
    closed_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        status = scan_port(host, port)
        if status == "open":
            open_ports.append(port)
        elif status == "closed":
            closed_ports.append(port)
        else:
            print(f"Port {port} is {status}.")
    #Returns  open_ports and closed_ports.
    return open_ports, closed_ports

def icmp_ping_sweep(network):
    
    # Function to perform an ICMP Ping Sweep on the given network.
    # Pings all addresses on the network (except network and broadcast addresses).
    # Prints the status of each host and counts the number of hosts online.
    
    ip = IP()
    icmp = ICMP()
    ip.dst = network

    hosts_online = 0

    for i in range(1, 255):
        ip.dst = network[:-1] + str(i)
        if ip.dst != network and ip.dst != network[:-1] + "255":
            response = sr1(ip / icmp, timeout=1, verbose=False)
            if response is None:
                print(f"Host {ip.dst} is down or unresponsive.")
            elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip.dst} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip.dst} is responding.")
                hosts_online += 1

    print(f"\nTotal hosts online: {hosts_online}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python network_security_tool.py <mode> <target>")
        sys.exit(1)

    mode = sys.argv[1]
    target = sys.argv[2]

    if mode == "TCP":
        # TCP Port Range Scanner mode
        if ":" in target:
            print("IPv6 is not supported in this mode.")
            sys.exit(1)
        try:
            host, port_range = target.split(":")
            start_port, end_port = map(int, port_range.split("-"))
        except ValueError:
            print("Invalid target format for TCP Port Range Scanner mode.")
            sys.exit(1)

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

    elif mode == "ICMP":
        # ICMP Ping Sweep mode
        if "/" not in target:
            print("Invalid target format for ICMP Ping Sweep mode.")
            sys.exit(1)

        try:
            network, cidr = target.split("/")
            cidr = int(cidr)
            if cidr < 8 or cidr > 30:
                print("Invalid CIDR block. Must be between 8 and 30.")
                sys.exit(1)
        except ValueError:
            print("Invalid target format for ICMP Ping Sweep mode.")
            sys.exit(1)

        if "." not in network:
            print("Invalid network address.")
            sys.exit(1)

        if ":" in network:
            print("IPv6 is not supported in this mode.")
            sys.exit(1)

        icmp_ping_sweep(network + "/" + str(cidr))

    else:
        print("Invalid mode. Use 'TCP' or 'ICMP'.")
        sys.exit(1)
