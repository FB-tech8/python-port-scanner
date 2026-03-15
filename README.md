# Python Port Scanner

This project is a simple TCP port scanner developed using Python.  
It scans ports on a target machine to identify open ports that are accepting connections.

## Features
- Scans TCP ports from 1 to 1024
- Detects open ports on the target host
- Demonstrates basic network security concepts
- Built using Python's socket library

## Technologies Used
- Python
- Socket Programming

## How It Works
The scanner attempts to establish a TCP connection to each port in the specified range.  
If the connection succeeds, the port is considered open.

## Example Output

Scanning target: 127.0.0.1  
Scanning ports 1-1024...

Port 135 is open  
Port 445 is open  

Scan completed.

## Files in This Project
- port_scanner.py → Python script for scanning ports
- scan_result.png → Screenshot showing the scanner running
- README.md → Project documentation

## Purpose
This project demonstrates basic cybersecurity concepts and network scanning techniques used to identify open ports on a host system.
