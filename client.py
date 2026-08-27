from ollama import chat
import socket


def get_reply(prompt):
    response = chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response.message.content


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for client...")

client, address = server.accept()
print("Client connected:", address)

while True:
    prompt = client.recv(1024).decode()

    if not prompt:
        break

    if prompt.lower() == "exit":
        break

    response = get_reply(prompt)

    client.send(response.encode())

client.close()
server.close()