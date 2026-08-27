from ollama import chat
import socket

def get_reply(prompt):
    
    response = chat(
        model='qwen2.5:3b',
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response.message.content

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for client...")

client, address = server.accept()
print("Client connected:", address)

prompt = client.recv(1024).decode()
responce = get_reply(prompt)

client.send(responce.encode())

client.close()
server.close()
