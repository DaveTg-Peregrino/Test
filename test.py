import socket

# Now, we have to answer four questions:
# 1. Internet socket or unix socket? Easy one, Internet socket
# 2. What kind of protocol (UCP or TCP)? UCP is for sensible data and UDP is faster than TCP. Here, TCP
# 3. Which IP are we going to use?
# 4. Which port are we going to use?

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This is TCP. UDP is SOCK_DGRAM
s.bind(('127.0.0.1', 55555)) #localhost, port
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()