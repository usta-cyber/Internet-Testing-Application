import requests
import socket

def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

# Function to get public IP address
def get_public_ip():
    response = requests.get("https://api.ipify.org")
    return response.text

print(f"Public IP Address:{get_public_ip()}")
print(f"Private IP Address:{get_private_ip()}")