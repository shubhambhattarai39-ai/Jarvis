import socket
import speech_recognition as sr
import pyttsx3

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

client.connect(("192.168.1.13", 5000))
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

while True:

    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
    
        print("Listening... Speak now!")
        audio_data = recognizer.listen(source)
        print("Processing audio...")

    try:
        prompt = recognizer.recognize_google(audio_data)
        print("You:", prompt)
        if prompt.lower() == "exit":
            client.send(prompt.encode())
            break
        client.send(prompt.encode())
        print("Getting data!!")
        data = client.recv(1024).decode()
        engine.say(data)
        engine.runAndWait()
        print("Jarvis:", data)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

client.close()
engine.stop()
