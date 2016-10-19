import socket

if(__name__ == "__main__"):
    print("Hello World!")

# 1. Create a socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. "Bind" the socket to an IP and PORT
my_socket.bind(("localhost", 3000))

# 3. Begin "listening" on the socket
my_socket.listen(5)


# 4. Begin "accepting" client connections
conn, addr = my_socket.accept()

while(True):

# 5. Receive some data (up to 1024 bytes) FROM the client
    data = ''
    data = conn.recv(1024)
    data_string = str(data)

    if not data: break
    conn.sendall(data)

    for i in range(0, len(data)):
        if(data_string[i] == "\\" and data_string[i+1] == "r" and data_string[i+2] == "\\" and data_string[i+3] == "n"):
            x = data_string[2:i]
            print(x)
            break


# 6. Send some data back TO the client
#conn.sendall("Hello Web Client!")
