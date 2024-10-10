import socket

# Target IP address and port
ip_address = "192.168.137.18"
port = 80  # Example: HTTP port

def ping_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Try to connect to the given port
        result = sock.connect_ex((ip, port))
        
        # If result is 0, the port is open
        if result == 0:
            print(f"Port {port} is open and reachable on {ip}")
        else:
            print(f"Port {port} is closed or unreachable on {ip}")
        # Close the socket
        sock.close()
    except Exception as e:
        print(f"Error connecting to {ip} on port {port}: {e}")

# Ping the specified port
ping_port(ip_address, port)
