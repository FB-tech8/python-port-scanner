import socket

target = input("Enter target IP address: ").strip()

# convert hostname to IP

print("Scanning target:", target)
print("Scanning ports 1-1024...\n")

for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
           print("Port", port, "is open")

    except:
        pass

    s.close()

print("\nScan completed.")

