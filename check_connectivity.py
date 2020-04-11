import requests
import socket

def check_host():
    localhost = socket.gethostbyname("localhost")
    if localhost == "127.0.0.1":
        return True
    else:
        return False

def check_connectivity():
    connection = requests.get("https://www.google.com")
    if connection.status_code == 200:
        return True
    else:
        return False

if check_host() or check_connectivity():
    print("Everything is okay!")
else:
    print("No network connection!")
