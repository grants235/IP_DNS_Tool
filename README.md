# IP/DNS Finder Tool

This is a tool that can take a list of subdomains and more reliably check if they are valid. It works by first checking all the subdomains and creating a list of IPs the domains resolve to. Then the script tries all of the valid IP aginst all of domains that would not resolve. This techineque finds more valid subdomains than just resolving the domain names beacuse some of the subdomains might not resolve to an IP but is still hosted on the same servers as other subdomains. 

![screenshot](https://github.com/grants235/IP_DNS_Tool/blob/master/image_2021-01-07_090944.png?raw=true)

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
