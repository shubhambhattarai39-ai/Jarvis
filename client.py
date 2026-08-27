import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sent_request = False

client.connect(("192.168.1.13", 5000))
while sent_request == False:
    
    prompt = str(input("Enter prompt: "))

    client.send(prompt.encode())
    sent_request = True

data = client.recv(1024).decode()
print("Jarvis:", data)

client.close()