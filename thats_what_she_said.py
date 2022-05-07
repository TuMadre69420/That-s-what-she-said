from gtts import gTTS
import speech_recognition as sr
import os
import smtplib
import time
r = sr.Recognizer()
m = sr.Microphone()
she = gTTS(text="That's what she said", lang="en", slow=False)
she.save("she.mp3")
o = smtplib.SMTP_SSL("smtp.gmail.com", 465)
print("To fully enjoy this program,")
print("go to your google account settings and enable access for less secure apps.")
print("Feel free to disable access after you're done")
while True:
    print("Enter your email")
    user = input(">").strip()
    print("Enter your password")
    password = input(">").strip()
    try:
        o.login(user, password)
        break
    except:
        print("Incorrect password")
print("Try saying something sus")
print("Loading in")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
while True:
    with m as source:
        print("Recording...")
        a = r.listen(source)
        print("Processing...")
        try:
            t = r.recognize_google(a).lower()
            print(t)
            if "it's so big" or "it's so long" or "it's kinda long" or "it is so big" or "it is so long" or "it is kind of long" or "it is kinda long" or "daddy" or "fuckin" or "frickin" or "fucking" or "fricking" or "is that long" or "that's long" or "oh yeah" in t:
                os.system("she.mp3")
                o.sendmail("minor69ner420@gmail.com", user, "That's what she said")
        except:
            print("Sorry, please try again")


        
