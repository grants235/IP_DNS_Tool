import sys
import socket 
import requests

print("-----------")
print("IP/DNS Tool")
print("-----------")

# Checks to see if host file is supplied
hosts=[]
valid_ips=[]
if(len(sys.argv) != 2):
    print("no hosts found.")
    exit()  

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
        r = requests.head(schema+host.strip()+"/", timeout=2)
        statusCode = r.status_code
        statusMessage = r.reason
        status = str(statusCode) + " " + statusMessage
        return(status)
    except:
        return("FAILED")


hosts_file = open(sys.argv[1],'r')
for host in hosts_file:
    hosts.append(host.strip())
    failed = 0
    
    
    # Getting IP address to http://<host>
    httpIP = getIpFromHost(host, 80)

    # Getting IP address to https://<host>
    httpsIP = getIpFromHost(host, 443)
     
    # Getting status code for http://<host>
    httpStatusCode = getStatusCode(host, 80)
    
    # Getting status code for https://<host>
    httpsStatusCode = getStatusCode(host, 443)
    
    
    
    # Processes http IP
    if httpIP != "1.1.1.1" and httpIP not in valid_ips and httpIP != "FAILED":
        valid_ips.append(httpIP)
        
    # Processes https IP    
    if httpsIP != "1.1.1.1" and  httpsIP not in valid_ips and httpsIP != "FAILED":
        valid_ips.append(httpsIP)


    
    print("Hostname : "+host.strip()) 
    print("IP (80): "+ httpIP) 
    print("IP (443): "+ httpsIP)
    print("Status Code (80): ", httpStatusCode)
    print("Status Code (443): ", httpsStatusCode)
    print("\n")
    
    
hosts_file.close()


output1=open("output1_IPs.txt", "w")
for ip in sorted(valid_ips):
    output1.write(ip)
    output1.write("\n")
output1.close()