# IP/DNS Finder Tool

This is a tool that can take a list of subdomains and more reliably check if they are valid. It works by first checking all the subdomains and creating a list of IPs the domains resolve to. Then the script tries all of the valid IP aginst all of domains that would not resolve. This techineque finds more valid subdomains than just resolving the domain names beacuse some of the subdomains might not resolve to an IP but is still hosted on the same servers as other subdomains. 

## Requrements

1. Python 3.7

## Usage

> python main.py <file of hosts newline seperated>