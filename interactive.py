url = "http://www.google.com"
timeout = 5
net=1
while True:
    try:
        import requests
        request = requests.get(url, timeout=timeout)
        break
    except (requests.ConnectionError, requests.Timeout) as exception:
        import playsound
        if net==1:
            with open("net.mp3"):
                playsound.playsound("net.mp3")
                net=5
import speech_recognition as sr     #pip install SpeechRecognition
import pyttsx3   #pip install pyttsx3
from gtts import gTTS  #pip install gTTS
import os
import geocoder
import cv2
import face_recognition
import time
import requests,json
import playsound     #pip install playsound
import webbrowser
from twilio.rest import Client #for sending text messages (pip install twilio)
import pywhatkit as po
import pyautogui as gui
import numpy as np
import smtplib #Simple Mail Transfer Protocol (pip install secure-smtplib)
from email.message import EmailMessage
face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Sender_Email = "hempuppala@gmail.com" 
Reciever_Email = "hemanthpuppala777@gmail.com"  
Password = "ctcskjezlwyfmvei"
video=cv2.VideoCapture(0)
r = sr.Recognizer()
#recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
#recognizer.read('trainer/trainer3.yml')   #load trained model
x=1
import datetime
user="hemanth"
api_key = "ba2cecb4088affa01522866c33d92db6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
time=datetime.datetime.now().strftime("%H %M")   #Present date and time
hour=int(datetime.datetime.now().hour)
minute=int(datetime.datetime.now().minute)
minute=minute+2
client = Client("AC51b5f2ac0aa87082f1ff89c0470225ef", "0d12c51f78857104a75656a5d6f8729f") #auth token and ssid of twilio(can find in twilio.com)
from_no ='+15162899361'
numbers_to_message = ['+918790 078 951', '+917013422733']
houras=str(datetime.datetime.now().hour)
minuteas=str(datetime.datetime.now().minute)
time=houras+" "+minuteas
def pub(absd):
    from Nodemcuu import pubData as a
    a.publish(absd)
while True:
    try:
        def videos():
            check,frame=video.read()
            frame = cv2.resize(frame, (600,400))
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            return frame
        if x==1:
            tts = gTTS("Hello"+user+" this is jarvis")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            x=x+1
            print("s") 
        with sr.Microphone() as source2:  
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            h = MyText.lower()
        print(h)
        if "what" in h and "time" in h:
            tts = gTTS("It is"+time)
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            if int(hour)<12:
                tts = gTTS("Good morning")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
            elif int(hour)<12 and int(hour)<16:
                tts = gTTS("Good afternoon")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
            else:
                tts = gTTS("good evening")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
        elif "open" in h and "notepad" in h:
            tts = gTTS("What do you want to write in the notes")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            tts = gTTS("what is the name of the note")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                aw = MyText.lower()
            with open(aw+'.txt', 'w') as f:
                f.write(asd)
                print("done")
        elif "notes" in h or "note" in h and "read" in h:
            try:
                tts = gTTS("what is the name of the note")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    aw = MyText.lower()
                with open(aw+'.txt', 'r') as f:
                    con=f.read()
                    print(con)
                    tts = gTTS(con)
                    tts.save('hem.mp3')  #creating a audio file containing the above text
                    playsound.playsound('hem.mp3')  #playing sound
                    os.remove('hem.mp3')
            except:
                tts = gTTS(f"Sorry{user}, there is no such file in my database")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
        elif "delete" in h and "note" in h:
            tts = gTTS("Which note do you want to delete")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                aw = MyText.lower()
            os.remove(aw+".txt")
        elif h=="close notepad":
            os.system("taskkill /f /im notepad.exe")
        elif h=="close chrome" or h=="close google chrome":
            print("c")
            os.system("taskkill /f /im chrome.exe")
        elif "chrome" in h or "google chrome" in h and "close" not in h:
            print("o")
            z="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Google Chrome.lnk"
            os.startfile(z)
        elif h=="close whatsapp":
            os.system("taskkill /f /im WhatsApp.exe")
        elif "open" in h and "whatsapp" in h and "message" not in h:
            x="C:/Users/puppa/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/WhatsApp/WhatsApp.lnk"
            os.startfile(x)
        elif "command prompt" in h:
            os.system("start cmd")
        elif "camera" in h:
            while True:
                frame=videos()
                cv2.imshow('asff' , frame)
                a=cv2.waitKey(1)
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    m = MyText.lower()
                print(m+"a")
                if m=="close camera"or m=="close":
                    cv2.destroyAllWindows()
                    break
                else:
                    tts = gTTS("You need to close the camera first")
                    tts.save('hem.mp3')  #creating a audio file containing the above text
                    playsound.playsound('hem.mp3')  #playing sound
                    os.remove('hem.mp3')
        elif h=="close camera":
            cv2.destroyAllWindows()
        elif "google" in h or "what is" in h or "search for" in h or "what do you mean by" in h and "weather" not in h and "temperature" not in h and "forecast" not in h:
            tts = gTTS("What do you want to search for")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                m = MyText.lower()
            print(m)
            webbrowser.open("https://www.google.com/search?q="+m)
        elif "open" in h and "youtube" in h and "play" not in h:
            webbrowser.open("https://www.youtube.com")
        elif "whatsapp" in h and "message" in h:
            hours=int(datetime.datetime.now().hour)
            minutes=int(datetime.datetime.now().minute)
            tts = gTTS("What is the message")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            po.sendwhatmsg("+917013422733",f"{asd}",hours,minutes+2)
            gui.press('enter')
        elif "send message" in h or "send a message" in h:
            tts = gTTS("What is the message")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            for number in numbers_to_message:
                
                client.messages.create(                    
                            body=f"{asd}",
                            from_ = from_no,
                            to = number
                                        )
                tts = gTTS("done")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
        elif "emergency" in h:
            for number in numbers_to_message:
               
                client.messages.create(                    
                            body="EMERGENCY!!!",
                            from_ = from_no,
                            to = number
                                        )
            tts = gTTS("Emergency note sent")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
        elif "send mail" in h or "send email" in h:
            tts = gTTS("What is the content of the email")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            newMessage = EmailMessage()                         
            newMessage['Subject'] = asd 
            newMessage['From'] = Sender_Email
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content(f"{asd}")
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:    #SMTP to operate using Secure Sockets Layer (SS                
                smtp.login(Sender_Email, Password)  #Logging into mail
                smtp.send_message(newMessage)   #Sending mail
            print("Mail sent!")
        elif "play song" in h or "play a song" in h:
            os.system("taskkill /im chrome.exe /f")
            tts = gTTS("Which song do you wanna play")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            try:
                po.playonyt(f"{asd}")
            except:
                print('cant reach')
        elif "play a video" in h or "any video" in h:
            tts = gTTS("Which video do you wanna play")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            try:
                po.playonyt(f"{asd}")
            except:
                print('cant reach')
        elif "unlock" in h:
            frame=videos()
            hours=str(datetime.datetime.now().hour)
            minutes=str(datetime.datetime.now().minute)
            sec=str(datetime.datetime.now().second)
            ptime=hours+minutes+sec
            known_image = face_recognition.load_image_file("user.jpg")
            print(ptime)
            #cv2.imshow('asd',frame)
            cv2.imwrite(ptime+".jpg", frame)
            try:
                unknown_image = face_recognition.load_image_file(ptime+".jpg")
                biden_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                print(results)
                if results==[True]:
                    os.remove(ptime+".jpg")
                    pub('off')
                    tts = gTTS("Door unlocked")
                    tts.save('hem.mp3')  #creating a audio file containing the above text
                    playsound.playsound('hem.mp3')  #playing sound
                    os.remove('hem.mp3')
                else:
                    tts = gTTS("Sorry i cant recognize you")
                    tts.save('hem.mp3')  #creating a audio file containing the above text
                    playsound.playsound('hem.mp3')  #playing sound
                    os.remove('hem.mp3')
                    pub('onn')
                a = cv2.waitKey(1)
            except:
                print("No face detected")
                tts = gTTS("No face detected")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
        elif "take picture" in h or "take a picture" in h:
            frame=videos()
            print(time)
            cv2.imwrite(time+".jpg",frame)
            #cv2.imshow(time+".jpg",frame)
            #cv2.waitKey(1)
            tts = gTTS("Picture saved")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
        elif "weather" in h or "forecast" in h or "temperature" in h:
            tts = gTTS("at which city do you want to know the weather conditions?")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                asd = MyText.lower()
            complete_url = base_url + "appid=" + api_key + "&q=" + asd
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                temp=current_temperature-273.15
                temp=(format(temp,".2f"))
                if current_pressure>950 and current_pressure<1050:
                    press="Normal"
                elif current_pressure<950:
                    press="less which may lead to cloudiness, wind, and precipitation"
                else:
                    press="High which may lead to rise in temperature"
                if current_humidity<60 or current_humidity>30:
                    hum="Normal"
                elif current_humidity>=60:
                    hum="too High"
                else:
                    hum="Too Low"
                tts = gTTS(f"Temperature is {temp} degrees celsius. Atmospheric Pressure is {press}. Humidity is{current_humidity}percent which is {hum}. These are causing  {weather_description} in {asd}")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
            else:
                tts = gTTS(f"Sorry i cant find the Weather conditions in {asd} ")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
        elif h=="set alarm":
            from alarm import alarm
            dates=datetime.datetime.now().strftime("%Y-%m-%d")   #Present date and time
            print(dates)
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                m = MyText.lower()
            hour=m
            print(hour)
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                nma = MyText.lower()
            minu=nma
            print(minu)
            times=hour+":"+minu
            print(times)
            with sr.Microphone() as source2:  
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                nm = MyText.lower()
            name=nm
            print(name)
            alarm.alarm(name,times,dates)
        elif "increase" in h or "up" in h and "volume" in h:
            for i in range (5):
                gui.press("volumeup")
        elif "full" in h or "high" in h and "volume" in h:
            for i in range (50):
                gui.press("volumeup")
        elif "decrease" in h or "down" in h and "volume" in h:
            for i in range (10):
                gui.press("volumedown")
        elif "mute" in h and "volume" in h:
            gui.press("volumemute")
        elif "pause" in h or "stop" in h or "pause the song" in h:
            gui.press("space")
        elif "location" in h or "where am i" in h:
            ip = geocoder.ip("me")
            p=ip.city
            tts = gTTS(f"You are in {p}")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
        elif "turn on light" in h:
            pub('twoon')
        elif "turn off light" in h:
            pub('twooff')
        elif "turn on fan" in h:
            pub('fanon')
        elif "turn off fan" in h:
            pub('fanoff')
        elif "sleep" in h:
            tts = gTTS(f"you can wake me up at any time {user}")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')
            while True:
                with sr.Microphone() as source2:  
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    asd = MyText.lower()
                if "wake" in asd:
                    tts = gTTS("Yes sir, how can i help you?")
                    tts.save('hem.mp3')  #creating a audio file containing the above text
                    playsound.playsound('hem.mp3')  #playing sound
                    os.remove('hem.mp3')
                    break
        elif "goodbye" in h:
            break
        else:
            tts = gTTS("please repeat again")
            tts.save('hem.mp3')  #creating a audio file containing the above text
            playsound.playsound('hem.mp3')  #playing sound
            os.remove('hem.mp3')

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        with open("net.mp3"):
            playsound.playsound("net.mp3")
        while True:
            try:
                request = requests.get(url, timeout=timeout)
                tts = gTTS("Connected to the internet, Now you can continue")
                tts.save('hem.mp3')  #creating a audio file containing the above text
                playsound.playsound('hem.mp3')  #playing sound
                os.remove('hem.mp3')
                break
                #print("Connected to the Internet")
            except (requests.ConnectionError, requests.Timeout) as exception:
                net=6

    
    except sr.UnknownValueError:
        continue
