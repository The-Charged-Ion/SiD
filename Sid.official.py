def kill():
      import time
      print("B")
      time.sleep(0.5)
      print("Y")
      time.sleep(0.5)
      print("E")
      time.sleep(0.5)
      print("!")
      exit()
import datetime
import time
import webbrowser
import subprocess
import os
import importlib
print("Hello Boss!")
time.sleep(1.2)
print("How can I Help You?")
time.sleep(1)
#Day and Month
day = ""
mont = ""
if str(datetime.datetime.now())[5:7]=='01':
      mont = 'January'
if str(datetime.datetime.now())[5:7]=='02':
      mont = 'February'
if str(datetime.datetime.now())[5:7] =='03':
      mont = 'March'
if str(datetime.datetime.now())[5:7] =='04':
      mont = 'April'
if str(datetime.datetime.now())[5:7]=='05':
      mont = 'May'
if str(datetime.datetime.now())[5:7]=='06':
      mont = 'June'
if str(datetime.datetime.now())[5:7]== '07':
      mont = 'July'
if str(datetime.datetime.now())[5:7]=='08':
      mont = 'August'
if str(datetime.datetime.now())[5:7]=='09':
      mont = 'September'
if str(datetime.datetime.now())[5:7]=='10':
      mont = 'October'
if str(datetime.datetime.now())[5:7]=='11':
      mont = 'November'
if str(datetime.datetime.now())[5:7]=='12':
      mont = 'December'
if str(datetime.datetime.now())[8:10] == '01':
      day = str(datetime.datetime.now())[8:10] + 'st'
if str(datetime.datetime.now())[8:10] == '02':
      day = str(datetime.datetime.now())[8:10] + 'nd'
if str(datetime.datetime.now())[8:10] == '03':
      day = str(datetime.datetime.now())[8:10] + 'rd'
else:
      day = str(datetime.datetime.now())[8:10] + 'th'
daymon = "Today is The " + day + ' of  ' + mont
print(daymon)
#End of Day and Month
a = 1
b = 4
answer = " "
#The While loop Which Continues The Input Option in The Actual Program
while a != b:
      time.sleep(0.5)
      #The First Input Bug
      chat = input("Chat... ")
      answer = " "
      #And the Large Ladder of If Statements:
      if chat == 'Hello!':
            answer =  "Hello Boss!"
      if "Hello" in chat:
            answer = "Hello Boss!"
      if "Hey" in chat:
            answer = "Hello Boss!"
      if 'How are you' in chat:
            answer = "Felling Amazing!"
      if 'how are you' in chat:
            answer = "Felling Amazing!"
      if 'how are u?' in chat:
            answer = "Felling Amazing!"
      
      if 'hello' in chat:
            answer = "Hello Boss!"
      if 'hey' in chat:
            answer = "Hello Boss!"
      if'hi' in chat:
            answer = "Hello Boss!"
      if 'shutup' in chat:
            print("Okay Boss!")
            time.sleep(0.6)
            kill()
      if 'What are you doing?' in chat:
            print("Chatting with You!")
      if 'what are you doing' in chat:
            print("Chatting with You!")
      if 'whatcha doing' in chat:
            print("Chatting with You!")
      if 'what are you doing?' in chat:
            print("Chatting with You!")
      if 'order food' in chat:
            print("Okay Boss")
            time.sleep(1)
            print("Rendering Brahmin's Thatte Idli Main page on swiggy")
            time.sleep(0.5)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.swiggy.com/restaurants/brahmins-thatte-idli-14th-main-a-block-sahakar-nagar-bangalore-110901')
      if 'date' in chat:
            print(daymon)
      if 'im hungry' in chat:
            print("Okay Boss")
            time.sleep(1)
            print("Rendering Brahmin's Thatte Idli Main page on swiggy")
            time.sleep(0.5)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.swiggy.com/restaurants/brahmins-thatte-idli-14th-main-a-block-sahakar-nagar-bangalore-110901')
      if "I'm Hungry!" in chat:
            print("Okay Boss")
            time.sleep(1)
            print("Rendering Brahmin's Thatte Idli Retro Main page on swiggy")
            time.sleep(0.5)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.swiggy.com/restaurants/brahmins-thatte-idli-14th-main-a-block-sahakar-nagar-bangalore-110901')
      if 'Order Food' in chat:
            print("Okay Boss")
            time.sleep(1)
            print("Rendering Brahmin's Thatte Idli Main page on swiggy")
            time.sleep(0.5)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.swiggy.com/restaurants/brahmins-thatte-idli-14th-main-a-block-sahakar-nagar-bangalore-110901')
      if 'i love you' in chat:
            print("I Love You Too!")
      if 'open whatsapp' in chat:
            print("Absolutely Boss!")
            time.sleep(0.5)
            print("Opening WhatsApp")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            a = subprocess.check_output ("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
      if 'check whatsapp' in chat:
            print("Absolutely Boss!")
            time.sleep(0.5)
            print("Opening WhatsApp")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            a = subprocess.check_output ("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
      if 'check my whatsapp' in chat:
            print("Absolutely Boss!")
            time.sleep(0.5)
            print("Opening WhatsApp")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            a = subprocess.check_output ("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
      if 'music' in chat:
            print("To Play Different music,\nType = play")
            time.sleep(1.5)
            webbrowser.open("https://youtu.be/J54re5Dfixs?t=22")
      if 'Music' in chat:
            webbrowser.open("https://youtu.be/J54re5Dfixs?t=22")
      if chat == 'disconnect wifi':
            print("Okay Boss!")
            time.sleep(0.5)
            print("System Overriding for Disconnection")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.check_output('netsh wlan disconnect')
            time.sleep(0.6)
            print("Done Boss!")
      if 'Weather' in chat:
            print('Sure Boss!')
            time.sleep(0.5)
            print("Rendering The HomePage of MSN Weather")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open("https://www.msn.com/en-in/weather/forecast?el=M6Xo6BO5tQvp8VZuDd68Br7O8S1S0mdnRIKZHfKJ9LEbf5uj7Mm8HvYr3J2yh8WN&ocid=ansmsnweather")
      if 'weather' in chat:
            print('Sure Boss!')
            time.sleep(0.5)
            print("Rendering The HomePage of MSN Weather")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open("https://www.msn.com/en-in/weather/forecast?el=M6Xo6BO5tQvp8VZuDd68Br7O8S1S0mdnRIKZHfKJ9LEbf5uj7Mm8HvYr3J2yh8WN&ocid=ansmsnweather")
      if 'stop' in chat:
            kill()
      if 'shutup' in chat:
            kill()
      if 'Shut up!' in chat:
            kill()
      if 'Stop!' in chat:
            kill()
      if 'my youtube' in chat:
            print("Sure Boss!")
            time.sleep(0.5)
            print("Opening Youtube")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.youtube.com/channel/UCYH6AdUvn9zfnqBKD5ol3TA')
      if chat == 'open My Youtube Channel':
            print("Sure Boss!")
            time.sleep(0.5)
            print("Opening Youtube")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://www.youtube.com/channel/UCYH6AdUvn9zfnqBKD5ol3TA')
      if 'Spotify' in chat:
            print("Sure Boss!")
            time.sleep(0.5)
            print("Opening Spotify MainPage")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen('C:\\Users\\Raman_b1j3bas\\AppData\\Roaming\\Spotify\\Spotify.exe')
      if 'spotify' in chat:
            print("Sure Boss!")
            time.sleep(0.5)
            print("Opening Spotify MainPage")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen('C:\\Users\\Raman_b1j3bas\\AppData\\Roaming\\Spotify\\Spotify.exe')
      if chat == 'play':
            chask = input("Enter what you want me to play: ")
            if 'ohno' in chask:
                  webbrowser.open('https://www.youtube.com/watch?v=ZOQRCZIfHBw')
            if 'Oh No' in chask:
                  webbrowser.open('https://www.youtube.com/watch?v=ZOQRCZIfHBw')
            if 'oh no' in chask:
                  webbrowser.open('https://www.youtube.com/watch?v=ZOQRCZIfHBw')
            if 'believer' in chask:
                  webbrowser.open("https://www.youtube.com/watch?v=W0DM5lcj6mw")
            if 'Believer' in chask:
                  webbrowser.open('https://www.youtube.com/watch?v=W0DM5lcj6mw')
            if 'Hymf for the Weekend' in chask:
                  webbrowser.open("https://www.youtube.com/watch?v=OflpZ6bgkVw")
            if 'hymn for the weekend' in chask:
                  webbrowser.open("https://www.youtube.com/watch?v=OflpZ6bgkVw")
            else:
                  print("Sorry.....")
                  time.sleep(1)
                  print("That song is not Present my Database.")
      if 'VS Code' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Initialising VS Code")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            subprocess.Popen("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      if '.vscode' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Initialising VS Code")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            subprocess.Popen("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      if 'vscode' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Initialising VS Code")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            subprocess.Popen("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      if 'My Website' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Opening Your Website's HomePage")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            webbrowser.open("http://127.0.0.1:5500/index.html")
      if 'web doveloping' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Initialising VS Code")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            subprocess.Popen("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      if 'web design' in chat:
            print("Sure Sir!")
            time.sleep(0.5)
            print("Initialising VS Code")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.8)
            print(".")
            time.sleep(0.4)
            subprocess.Popen("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      if 'new window' in chat:
            subprocess.Popen("C:\\Python34\\python.exe")
      if 'help me' in chat:
            print("Kindly Tell me your issue so that I can Help You!")
      if 'Help Me!' in chat:
            print("Kindly Tell me your issue so that I can Help You!")
      if chat == 'SID':
            print("Yes...")
      if chat == 'sid':
            print("Yes...")
      if 'py course' in chat:
            print("Yes Boss!")
            time.sleep(0.5)
            print("Initializing Python Course on Course")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            print("Initialized")
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe  --profile-directory=Default --app-id=oflpofniahomlkfigohbbcppfippndpk --app-url=https://www.coursera.org/learn/learn-to-program/home/welcome --app-launch-source=4")
      if 'learn python' in chat:
            print("Yes Boss!")
            time.sleep(0.5)
            print("Initializing Python Course on Course")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            print("Initialized")
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe  --profile-directory=Default --app-id=oflpofniahomlkfigohbbcppfippndpk --app-url=https://www.coursera.org/learn/learn-to-program/home/welcome --app-launch-source=4")
      if 'coursera' in chat:
            print("Yes Boss!")
            time.sleep(0.5)
            print("Initializing Python Course on Course")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            print("Initialized")
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe  --profile-directory=Default --app-id=oflpofniahomlkfigohbbcppfippndpk --app-url=https://www.coursera.org/learn/learn-to-program/home/welcome --app-launch-source=4")
      if 'Coursera' in chat:
            print("Yes Boss!")
            time.sleep(0.5)
            print("Initializing Python Course on Course")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            print("Initialized")
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe  --profile-directory=Default --app-id=oflpofniahomlkfigohbbcppfippndpk --app-url=https://www.coursera.org/learn/learn-to-program/home/welcome --app-launch-source=4")
      if 'msedge' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if 'Microsoft Edge' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if 'MS Edge' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if 'edge' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if 'open browser' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if 'browser' in chat:
            print("Okay Boss!")
            time.sleep(0.5)
            print('Rendering MS Edge')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)      
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
      if chat == 'SID':
            print('Yes.....')
      if 'search' in chat:
            sask = input("Search: ")
            answer = "Okay Boss!"
            time.sleep(0.5)
            print("Searching on the WEB.........")
            time.sleep(1)
            webbrowser.open(sask)
      if 'maths problem' in chat:
            print("What operation do you wanna carry out?")
            mask = input()
            if 'add' in mask:
                  answer = int(input("First Number: ")) + int(input("Second Number: "))
                  print("Calculating...")
                  time.sleep(1)
            if 'minus' in mask:
                  answer = int(input("First Number: ")) - int(input("Second Number: "))
                  print("Calculating...")
                  time.sleep(1)
            if 'divide' in mask:
                  answer = int(input("First Number: ")) / int(input("Second Number: "))
                  print("Calculating...")
                  time.sleep(1)
            if 'multiply' in mask:
                  answer = int(input("First Number: ")) * int(input("Second Number: "))
                  print("Calculating...")
                  time.sleep(1)
            if 'square' in mask:
                  answer = int(input("Number: ")) ** 2
                  print("Calculating...")
                  time.sleep(1)
            if 'cube' in mask:
                  answer = int(input("Number: ")) ** 2
                  print("Calculating...")
                  time.sleep(1)
            if 'expo' in mask:
                  print(int(input("First Number: ")) ** int(input("Second Number: ")))
                  print("Calculating...")
                  time.sleep(1)
      if 'youtube channel' in chat:
            yask = input("Which Channel on YouTube: ")
            webbrowser.open("https://youtube.com/" + yask)
      if 'Thanks' in chat:
            answer = "My Pleasure Boss!"
      if 'thanks' in chat:
            answer = "My Pleasure Boss!"
      if 'thx' in chat:
            answer = "My Pleasure Boss!"
      if 'import' in chat:
            imp_ask = input("Enter the Module you want to Import: ")
            try:
                  importlib.import_module(imp_ask)
            except ImportError:
                  print("Module Not found in Database")
      if 'Import ' in chat:
            imp_ask = input("Enter the Module you want to Import: ")
            try:
                  importlib.import_module(imp_ask)
            except ImportError:
                  print("Module Not found in Database")
      if 'wikihow' in chat:
            print("Sure Boss!")
            time.sleep(0.4)
            print("Rendering WikiHow's Home page")
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://wikihow.com/Main-Page')
      if 'WkiHow' in chat:
            print("Sure Boss!")
            time.sleep(0.4)
            print("Rendering WikiHow's Home page")
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            webbrowser.open('https://wikihow.com/Main-Page')
      if 'hate' in chat:
            print("I'm Extremely Sorry Boss!")
            time.sleep(1)
            print("If There is any Way I can Improve Myself,")
            time.sleep(0.8)
            print("Kindly type the Word 'Feedback' in the input bar So that I can Know where I am Wrong")
      if 'Hate' in chat:
            print("I'm Extremely Sorry Boss!")
            time.sleep(1)
            print("If There is any Way I can Improve Myself,")
            time.sleep(0.8)
            print("Kindly type the Word 'Feedback' in the input bar So that I can Know where I am Wrong")
      if 'HATE' in chat:
            print("I'm Extremely Sorry Boss!")
            time.sleep(1)
            print("If There is any Way I can Improve Myself,")
            time.sleep(0.8)
            print("Kindly type the Word 'Feedback' in the input bar So that I can Know where I am Wrong")
      #The Feedback Section      
      if 'Feedback' in chat:
            print("Sure Boss1")
            print("Your Feedback is Extremely Precious for Me!")
            time.sleep(2)
            print("But Boss,\nYou can Only give up to 3 FeedBacks")
            time.sleep(2.5)
            print("And to give all Feedbacks,\n Kindly Type 'more' in the Feedback swection for Being able to  Give More Feedback")
            time.sleep(2.6)
            feed1 = input("Feedback(1): ")
            feed = [feed1]
            if 'more' in feed1:
                  feed2 = input("Feedback(2): ")
                  feed = feed + [feed2]
                  if 'more' in feed2:
                        feed3 = input("Feedback(3): ")
                        feed = feed + [feed3]
                        if 'more' in feed3:
                              print("Sorry Boss!")
                              time.sleep(0.5)
                              print('I can only Take feedback up to 3 times.')
      if 'Show feedback' in chat:
            answer = feed[0]
            if feed1 in feed: 
                  answer = answer
                  if feed2 in feed:
                        answer = answer + '\n' + feed[1]
                        if feed3 in feed:
                              answer = answer + '\n' + feed[2]
      #end of Feedback Section
      if 'cmd' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'Command Prompt' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'command prompt' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'command Prompt' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'Command prompt' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'CMD' in chat:
            print("Initialsing Command Prompt")
            time.sleep(0.4)
            print(".")
            time.sleep(0.8)
            print('.')
            time.sleep(0.8)
            print('.')
            time.sleep(0.4)
            subprocess.Popen("C:\\WINDOWS\\System32\\cmd.exe")
      if 'minecraft' in chat:
            print("Initialising TLauncher")
            time.sleep(0.7)
            print("Done Boss!")
            time.sleep(0.8)
            subprocess.Popen("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
      if 'Minecraft' in chat:
            print("Initialising TLauncher")
            time.sleep(0.7)
            print("Done Boss!")
            time.sleep(0.8)
            subprocess.Popen("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
      if 'TLauncher' in chat:
            print("Initialising TLauncher")
            time.sleep(0.7)
            print("Done Boss!")
            time.sleep(0.8)
            subprocess.Popen("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
      if 'tlauncher' in chat:
            print("Initialising TLauncher")
            time.sleep(0.7)
            print("Done Boss!")
            time.sleep(0.8)
            subprocess.Popen("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
      if 'task manager' in chat:
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if chat == "what tasks are running on my pc":
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if 'Tasks Running on my PC' in chat:
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if 'Task Manager' in chat:
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if 'taskmgr' in chat:
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if 'show tasks' in chat:
            print("Sure Sir!")
            time.sleep(1)
            print("Here are the Tasks Running on your PC.\nThis may take a few seconds....")
            time.sleep(0.9)
            subprocess.check_output("taskmgr")
      if "Who is your Father?" in chat:
            print('Sir,')
            time.sleep(0.5)
            print("I Technically don't have a Father,.")
            time.sleep(0.367)
            print("I have A creator named Raman Varwani.")
            time.sleep(0.9)
            print("For giving your Complements to Dr.Raman Varwani")
            time.sleep(0.5)
            sid_feed = input("You can type Your Valuable feedback\nHere: ")
            if not sid_feed == "":
                  sid_feed_store = [sid_feed]
      if "Who is your Creator?" in chat:
                  print("Yes!")
                  time.sleep(0.5)
                  print("My Creator is Dr.Raman Varwani")
                  time.sleep(0.5)
                  print("For giving your Complements to Dr.Raman Varwani")
                  time.sleep(0.5)
                  sid_feed = input("You can type Your Valuable feedback\nHere: ")
      if "Mom's Laptop" in chat:
            print("Sure Boss!")
            time.sleep(0.5)
            print('Wow!\nThe Lenovo Ideapad!\nHonestly, Good choice sir.')
            webbrowser.open("https://www.amazon.in/Lenovo-IdeaPad-Warranty-Platinum-81WB01B0IN/dp/B09P1KJ37T/ref=sr_1_5?crid=3GBO59Y0KJ2JI&keywords=laptop%2B40000%2Bunder%2B512gb%2Bssd&qid=1650962335&sprefix=laptop%2B40000%2Bunder%2B512gb%2Bss%2Caps%2C206&sr=8-5&th=1")
      if "mom's laptop" in chat:
            print("Sure Boss!")
            time.sleep(0.5)
            print('Wow!\nThhie Lenovo Ideapad!\nHonestly, Good choice sir.')
            webbrowser.open("https://www.amazon.in/Lenovo-IdeaPad-Warranty-Platinum-81WB01B0IN/dp/B09P1KJ37T/ref=sr_1_5?crid=3GBO59Y0KJ2JI&keywords=laptop%2B40000%2Bunder%2B512gb%2Bssd&qid=1650962335&sprefix=laptop%2B40000%2Bunder%2B512gb%2Bss%2Caps%2C206&sr=8-5&th=1")
      if answer != " ":
                  print(answer)