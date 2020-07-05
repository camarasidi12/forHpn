from ipaddress import ip_address, IPv6Address
import sys

def check(ipFile):
         '''Check if an IP adress is correct or not'''

         correctIp = open("correct_ips.txt", "w")
         incorrectIp = open("incorrect_ips.txt", "w")
         
        #read ip from file
         with open(ipFile,"r") as f:
               for ip in f:
                    try:
                        v = ip_address(ip.strip())
                        correctIp.write(ip)
                    except ValueError:
                        incorrectIp.write(ip)
         correctIp.close()
         incorrectIp.close()
# Driver Code 
if __name__ == '__main__' : 
	#exit if no file is passed
    if len(sys.argv) < 2: 
        print("Please pass the input ip adress file")
        sys.exit(1)
        
    check(sys.argv[1]) 

