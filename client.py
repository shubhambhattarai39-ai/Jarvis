import socket
import speech_recognition as sr
import pyttsx3

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

recognizer = sr.Recognizer()

client.connect(("192.168.1.13", 5000))



def speak(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.9)

    voices = engine.getProperty("voices")

    # Try the first voice for now
    engine.setProperty("voice", voices[1].id)

    for voice in voices:
        if "GB" in voice.id or "United Kingdom" in voice.name or "Hazel" in voice.name:
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()
    engine.stop()

speak("Tero bau")

with sr.Microphone() as source:

    print("Adjusting for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:

        print("Listening... Speak now!")

        try:
            audio_data = recognizer.listen(source)

            print("Processing audio...")

            prompt = recognizer.recognize_google(audio_data)

            print("You:", prompt)

            if prompt.lower() == "exit":
                client.send(prompt.encode())
                break

            client.send(prompt.encode())

            print("Getting data...")

            data = client.recv(1024).decode()

            print("Jarvis:", data)

            speak(data)

        except sr.UnknownValueError:

            print("Sorry, I could not understand the audio.")

            speak("Sorry, I could not understand the audio.")


client.close()