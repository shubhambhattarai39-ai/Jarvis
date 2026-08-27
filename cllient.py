import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

prompt = str(input("Enter prompt: "))

client.send(prompt.encode())

data = client.recv(1024).decode()
print("Jarvis:", data)

client.close()