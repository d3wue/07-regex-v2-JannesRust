import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here


regv6 = re.compile("([0-9a-f]{4}:){7}([0-9a-f]{4})$")
regv4 = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})$")

ipv6Counter = 0 
ipv4Counter = 0
for ip in ipAddresses: 
    m = regv6.match(ip)
    m2 = regv4.match(ip)
    if m != None:
        ipv6Counter += 1
    if m2 != None:
        ipv4Counter += 1 

print(f"Es gibt {ipv4Counter} gülitge IPv4 Adressen")
print(f"Es gibt {ipv6Counter} gültige IPv6 Adressen")
    