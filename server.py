# Importing the socket module to create a socket for network communication
import socket  

# Defining the server's IP address and port number
SERVER_IP = '127.0.0.1'  # '127.0.0.1' is the loopback address (localhost)
SERVER_PORT = 65432       # Port number to listen for incoming connections

# Creating a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to the specified IP address and port number
server_socket.bind((SERVER_IP, SERVER_PORT))

# The server starts listening for incoming client connections
server_socket.listen(1)  
print("Server is listening for connections...")  # Print a message to indicate the server is ready

# Accepting a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")  # Print the client's address

# Infinite loop to keep the server running and handling messages
while (1):
    # Receiving a message from the client (up to 1024 bytes) and decoding it to a string
    message_from_client = client_socket.recv(1024).decode()  
    if not message_from_client:  # Check if the received message is empty (client disconnected)
        print("Client disconnected.")  # Print a message indicating the client has disconnected
        break  # Exit the loop

    print(f"Client: {message_from_client}")  # Print the message received from the client

    # Check if the client sent "exit" to close the connection
    if message_from_client == "exit":
        print("Client has exited the conversation.")  # Print a message indicating client exit
        break  # Exit the loop

    # Prompt the server user to enter a response message
    response_message = input("Server: Enter your message (type 'exit' to end): ")
    client_socket.send(response_message.encode())  # Send the response message to the client

    # Exit the loop if the server sends "exit"
    if response_message == "exit":
        print("Server has ended the conversation.")  # Print a message indicating server exit
        break  # Exit the loop

# Closing the client and server sockets
client_socket.close()  # Close the client socket
server_socket.close()  # Close the server socket
