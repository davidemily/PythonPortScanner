import socket, sys, time, datetime, os

choice = int(input("Enter 0 to scan machine by IP address"
                " or enter 1 to scan machine by hostname: "))

while choice < 0 or choice > 1:
    print("Did not choice one of the options")
    choice = input("Please choose 0 or 1")


if choice == 0:
    addr = input("Enter IP address you would like to scan: ")
elif choice == 1:
    hostname = input("Enter hostname you would like to scan: ")
    addr = socket.gethostbyname(hostname) #code uses IP address so use socket library to turn into IP

open_ports = []

startTime = time.time()

print("Beginning scanning on host: %s" % addr)
print()
print("Start time is: %s" % startTime)

for i in range(10000): #covers all important ports
    try:
        conn = socket.socket(family=AF_INET, type=SOCK_STREAM)
        conn.settimeout(0.7)
        attempt = conn.connect(address=addr, port=i)
        if attempt == 1:
            open_ports.append(i)
        attempt.close()
    except Exception:
        pass


totalTime = time.time() - startTime
print("Total time took is: %s" % totalTime)
if not open_ports:
    print("No ports open.")
    print("Host either has all ports closed or is offline.")
for port in open_ports:
    print("%s is open" % port)
