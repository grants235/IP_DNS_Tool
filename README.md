# IP/DNS Finder Tool

This is a tool that can take a list of subdomains and more reliably check if they are valid. It works by first checking all the subdomains and creating a list of IPs the domains resolve to. Then the script tries all of the valid IP aginst all of domains that would not resolve. This techineque finds more valid subdomains than just resolving the domain names beacuse some of the subdomains might not resolve to an IP but is still hosted on the same servers as other subdomains. 

## Note

***Please note that this is still a work in progess.***

As of now, it will resolve the subdomains and output a file. It also gets the HTTP status code and message but nothing else. See the to-do list down below.

## Requrements

- Python 3.7
- Required python modules (all inside the requirements.txt file for easy install):
    - requests

## Usage

``` 
python -m pip install requirements.txt
python main.py <file of hosts newline seperated>

 ```

## Other Information

- The host.txt and host2.txt files are demo files to show the format and test the script
- The ouput files are the files that the script creates. In this case, they are the output for the demo host files

## To-Do list 

- [x] Make DNS queries and get the IP address related to the subdomain list 
- [x] Get the HTTP status code and status message
- [x] Make output files of subdomains that work and subdomains that don't (working but still have a few false positives)
- Try every valid IP address with every subdomin that did not work on but was still found with the tools
