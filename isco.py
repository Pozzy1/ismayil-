import socket

# Target IP address and port
ip_address = "192.168.137.18"
port = 135  # Port you want to connect to

def connect_to_port(ip, port):
    try:
        # Create a socket object (TCP connection)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        
        # Try to connect to the specified port
        print(f"Attempting to connect to {ip}:{port}...")
        sock.connect((ip, port))
        print(f"Successfully connected to {ip}:{port}")
        
        # Once connected, you can send/receive data.
        # Example: Sending a basic message
        message = "Hello from Python!"
        sock.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Receiving a response (if the server sends one)
        response = sock.recv(1024)  # Adjust buffer size as needed
        print(f"Received: {response.decode('utf-8')}")
        
        # Close the connection after use
        sock.close()
    
    except Exception as e:
        print(f"Error connecting to {ip}:{port} - {e}")

# Connect to port 135
connect_to_port(ip_address, port)
