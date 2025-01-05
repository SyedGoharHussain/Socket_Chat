# Importing the socket module for network communication
import socket  

# Defining the server's IP address and port number to connect to
SERVER_IP = '127.0.0.1'  # '127.0.0.1' is the loopback address (localhost)
SERVER_PORT = 65432       # Port number to connect to the server

# Creating a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting the client socket to the server's IP address and port
client_socket.connect((SERVER_IP, SERVER_PORT))

# Infinite loop to keep the client running and sending messages
while (1):
    # Prompting the client user to enter a message to send to the server
    message_to_server = input("Client: Enter your message (type 'exit' to end): ")
    client_socket.send(message_to_server.encode())  # Send the message to the server

    # Check if the client wants to exit the conversation
    if message_to_server == "exit":
        print("Client has ended the conversation.")  # Print a message indicating client exit
        break  # Exit the loop 

    # Receiving the server's response and decoding it to a string
    response_from_server = client_socket.recv(1024).decode()
    if not response_from_server:  # Check if the received message is empty (server disconnected)
        print(f"Server disconnected.")  # Print a message indicating the server has disconnected
        break  # Exit the loop

    print("Server: {response_from_server}")  # Print the response received from the server

    # Break the loop if the server has sent "exit"
    if response_from_server == "exit":
        print("Server has ended the conversation.")  # Print a message indicating server exit
        break  # Exit the loop

# Closing the client socket
client_socket.close()  # Close the client socket
