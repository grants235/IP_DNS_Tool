import sys
import socket 
import requests

with open('./ascii_art.txt', 'r') as f:
    print(f.read())
    
    
def getIpFromHost(hostname, port):
    try:
        host_ip = socket.getaddrinfo(hostname.strip(), port)
        ip = host_ip[0][4][0]
        if ip == "1.1.1.1":
            raise Exception()
        return(ip)
    except:
        return("FAILED")

def getStatusCode(hostname, port):
    if port == 80:
        schema = "http://"
    if port == 443:
        schema = "https://"
    try:
        r = requests.head(schema+host.strip()+"/", timeout=2, verify=False)
        statusCode = r.status_code
        return(statusCode)
    except:
        return("FAILED")
    
def getStatusMessage(hostname, port):
    if port == 80:
        schema = "http://"
    if port == 443:
        schema = "https://"
    try:
        r = requests.head(schema+host.strip()+"/", timeout=2, verify=False)
        statusMessage = r.reason
        return(statusMessage)
    except:
        return("FAILED")
    
def listToFile(fileName, list):
    output=open(fileName, "w")
    for item in sorted(list):
        output.write(item)
        output.write("\n")
    output.close()
    return

# Checks to see if host file is supplied
hosts=[]
valid_hosts=[]
valid_ips=[]
invalid_hosts=[]
if(len(sys.argv) != 2):
    print("no hosts found.")
    exit()  
    

hosts_file = open(sys.argv[1],'r')
for host in hosts_file:
    hosts.append(host.strip())
    
    
    # Getting IP address to http://<host>
    httpIP = getIpFromHost(host, 80)

    # Getting IP address to https://<host>
    httpsIP = getIpFromHost(host, 443)
     
    # Getting status code for http://<host>
    httpStatusCode = getStatusCode(host, 80)
    httpStatusMessage = getStatusMessage(host, 80)
    
    # Getting status code for https://<host>
    httpsStatusCode = getStatusCode(host, 443)
    httpsStatusMessage = getStatusMessage(host, 443)
 
    
    # Adds IP address to master lists
    if httpIP != "1.1.1.1" and httpIP not in valid_ips and httpIP != "FAILED":
        valid_ips.append(httpIP)
    if httpsIP != "1.1.1.1" and  httpsIP not in valid_ips and httpsIP != "FAILED":
        valid_ips.append(httpsIP)

    # Add domains to master lists
    if httpsIP in valid_ips and httpsStatusCode != 400 and host not in valid_hosts:
        valid_hosts.append(host.strip())
    if httpsIP == "FALIED" or httpsStatusCode == 400 or httpsStatusCode == "FAILED" and host not in invalid_hosts:
        invalid_hosts.append(host.strip())
    
    # Prints out results
    print("Hostname : "+host.strip()) 
    print("IP (80): "+ httpIP) 
    print("IP (443): "+ httpsIP)
    print("Status Code (80): ", httpStatusCode)
    print("Status Code (443): ", httpsStatusCode)
    print("\n")
    
hosts_file.close()

# Creates and writes the output files
listToFile("output1_IPs.txt", valid_ips)
listToFile("output2_suscessful_subdomains.txt", valid_hosts)
listToFile("output3_failed_subdomains.txt", invalid_hosts)




