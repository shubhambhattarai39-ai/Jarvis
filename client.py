import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.1.13", 5000))

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        client.send(prompt.encode())
        break

    client.send(prompt.encode())

    data = client.recv(1024).decode()

    print("Jarvis:", data)

client.close()