import subprocess
import webbrowser as web
import datetime
import speech_recognition as sr  
import pyttsx3
import wikipedia
import os
import pyjokes
import sys
import time
import pywikihow as wh
from bs4 import BeautifulSoup as BS
import requests
from playsound import playsound
def say(audio):
    Engine = pyttsx3.init('sapi5')
    voices = Engine.getProperty('voices')
    Engine.setProperty('voice', voices[0].id)
    Engine.say(audio)
    Engine.runAndWait()
def takeCommand():
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = ear.listen(source)
        try: 
            ear.recognize_google(audio)
            print("Recognizing....")
        except Exception:
            print("I didn't get that...")
    text = ear.recognize_google(audio)
    print("User Said: ", text)
    return text
def getDate():
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
        day = "01"
    if str(datetime.datetime.now())[8:10] == '02':
        day = "02"
    if str(datetime.datetime.now())[8:10] == '03':
        day = "03"
    else:
        day = str(datetime.datetime.now())[8:10]
    daymon = "Today is The " + day + ' of  ' + mont
    say(daymon)
def WishMe():
    ghante = int(datetime.datetime.now().hour)
    if ghante > 0 and ghante < 12:
        say("Good Morning Sir!")
    elif ghante > 12 and ghante < 16:
        say("Good Afternoon Sir!")
    else:
        say("Good Evening Sir!")
    getDate()
def openPage(url):
    web.register('edge', None, web.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
    web.get('edge').open(url)
def SearchYT(): 
    say("What do you Want me to Search on youtube?")
    yt_search = takeCommand().lower()
    searched = "https://www.youtube.com/results?search_query=" + yt_search
    if yt_search != "nothing" and yt_search != "none":
        say("Searching Youtube")
        openPage(searched)
    else:
        say("Okay Sir!")
def getTemp(asked):
    url_page = f"https://www.google.com/search?q={asked}"
    req = requests.get(url_page)
    forecast = BS(req.text, "html.parser")
    temp = forecast.find("div", class_="BNeawe").text
    say(f"current {asked} is {temp}")
def SearchStackO(): 
    say("What do you Want to Search on stack overflow.com")
    STACKER = takeCommand().lower()
    stackOpen = "https://www.stackoverflow.com/search?q=" + STACKER
    try:
        if STACKER != "nothing" and STACKER != "none":
            say("Searching Stack Overflow")
            openPage(stackOpen)
        else:
            say("Okay Sir!")
    except Exception:
        say("Some Error Occured")
def getNumber(name):
    imp_num_dict = {
        "mum":"+919743432400",
        "dad":"+919743994449",
        "nani":"+918087171909",
        "masi":"+919930281815"
    }
    try:
        print(imp_num_dict[name])
        say(imp_num_dict[name])
    except Exception:
        say("The Number is Not Present in Your Contacts")
def searchGoogle(whattosearch):
    openPage(f"https://www.google.com/search?q={whattosearch}")
def searchAmazon():
    say("Amazon mode Activated")
    say("What should I Search on Amazon?") 
    try:
        search_amazon_what = takeCommand().lower()
        # if search_amazon_what != "nothing" and search_amazon_what != "none":
        req = requests.get(f"https://www.amazon.in/s?k={search_amazon_what}")
        h = BS(req.text, 'html.parser')
        full = h.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").text
        say("I Found a Result")
        say(full)
        # say("The Price is ")
        # price = h.find('span', class_="a-price-whole").text
        # say(price)
    except Exception:
        say("No sir, an Error Occured")
    else:
        say("Okay Sir!")
def SearchBing(what_toSearch):
    openPage(f"https://www.bing.com/search?q={what_toSearch}")
def getNews():
    url_news = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    req = requests.get(url_news)
    written = BS(req.text, 'html.parser')
    news = written.find("a", class_="DY5T1d RZIKme").text
    say("Todays Headline is")
    say(news)
    say("This is Provided by")
    provider = written.find("a", class_="wEwyrc AVN2gc uQIVzc Sksgp").text
    say(provider)
    news_subline = written.find("h4", class_="ipQwMb ekueJc RD0gLb").text
    say("and")
    say(news_subline)
def WhoIs(He):
    try:
        results = wikipedia.summary(He, sentences=2)
        say(results)
    except Exception:
        say("Sorry, There is Some Issue")
def getSportsNews():
    urlSports = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    req = requests.get(urlSports)
    w = BS(req.text, 'html.parser')
    sports__ = w.find('a', class_="DY5T1d RZIKme").text
    sports__Provider = w.find('a', class_="wEwyrc AVN2gc uQIVzc Sksgp").text
    say("Todays Sports Headlines are")
    say(sports__)
    say("This is Provided by")
    say(sports__Provider)
def getTechUpdate():
    url_tech = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    req = requests.get(url_tech)
    w = BS(req.text, "html.parser")
    tech_upD = w.find('a', class_="DY5T1d RZIKme").text
    tech_upD_Provider = w.find('a', class_="wEwyrc AVN2gc uQIVzc Sksgp").text
    say("Tech Updates now")
    say(tech_upD)
    say("Provided by")
    say(tech_upD_Provider)
def ExecuteSid():
    say("I am Ready and Online Sir!")
    while True:
        try:
            ask = takeCommand().lower()
        except Exception:
            continue
        if "open youtube" in ask:
            openPage("https://youtube.com")
        elif "wikipedia" in ask:
            say("Searching Wikipedia....")
            ask = ask.replace("wikipedia", "")
            try:
                results = wikipedia.summary(ask, sentences=2)
                say("According to Wikipedia...")
                say(results)
            except Exception:
                say("Sorry, There is no such Wikipedia page")
        elif "shut up" in ask:
            say("Okay Sir!")
            say("Bye")
            break
        elif "play music" in ask:
            say("What should I play Sir?")
            try:
                music_ask = takeCommand().lower()
            except Exception:
                say("Some Error")
                continue
            if "believer" in music_ask:
                playsound("Believer_.mp3")
            elif "the weekend" in music_ask:
                playsound("HymnForTheWeekend_.mp3")
            elif "calm music" in music_ask:
                playsound("calmMusic.mp3")
        elif "show tasks" in ask:
            subprocess.check_output("taskmgr")
        elif "tell me a story" in ask:
            say("Okay Sir!")
            say("Once upon a Time, A Fro Kingdom's King Organized a Competition.")
            say("He said, Anyone who Participates and Wins in this Competion of Climbing a Mountain,")
            say("Will get The Throne After Me.")
            say("Everybody Tried Very Hard!")
            say("But Couldnt Complete")
            say("And Started Saying that its Impossible")
            say("But Just then, A Deaf Frog Came and Unknowingly that Its a Competition, He Climbed to the Top of the Mountain")
            say("Everybody got Shocked!")
            say("The Moral is")
            say("People will say That its Impossible, But you Should have the Guts to prove them wrong.")
        elif 'how are you' in ask:
            say("Very Happy Sir!")
        elif 'hi' in ask:
            say("Hello Boss!")
        elif "open code" in ask:
            os.startfile("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "open command prompt" in ask:
            os.startfile("C:\\WINDOWS\\System32\\cmd.exe")
        elif "you are smart" in ask:
            say("Thank You Sir!")
        elif "sid" in ask:
            say("Yes Boss?")
        elif "search" in ask:
            ask = ask.replace("search", "")
            searchGoogle(ask)
        elif "open minecraft" in ask:
            os.startfile("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
        elif "open ti launcher" in ask:
            os.startfile("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
        elif "the time" in ask:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(str_time)
        elif "open source code" in ask:
            say("Okay sir")
            say("Opening My Source code")
            os.startfile("C:\\Users\\Raman_b1j3bas\\Desktop\\SID\\sid2.py")
        elif "you are funny" in ask:
            say('Thank You Sir!')
        elif "me a joke" in ask:
            joke = (pyjokes.get_joke())
            print(joke)
            say(joke)
        elif "quit" in ask:
            say("Okay Sir!")
            say("Bye")
            sys.exit()
        elif "what are you doing" in ask:
            say("Sir! I am Checking for some bugs Inside my Source Code")
            say("What about you?")
            try:
                haalchaal = takeCommand().lower()
            except Exception:
                say("Sorry! Some Problem Happened")
                continue
            if "talking to you" in haalchaal:
                say("Nice one Sir!")
            elif "nothing" in haalchaal:
                say("Sir! Why Dont you Complete the whatsapp Insertion in My Source code?")
            elif "homework" in haalchaal:
                say("Okay Sir!")
                say("If you need Any Help, Just ask me!")
            elif "testing you" in haalchaal:
                say("Okay! Sir!")
            else:
                say("Okay sir!")
        elif "thank you" in ask:
            say("My Pleasure Sir!")
        elif "thanks" in ask:
            say("My Pleasure Sir!")
        elif "what is your name" in ask:
            say("I am Sid!")
            say("Your Personal Assistant.")
        elif "close browser" in ask:
            try:
                subprocess.check_output("TASKKILL /f /IM msedge.exe")
            except Exception as e:
                say("It is already Closed Sir!")
        elif "you are so cool" in ask:
            say("Thanks a lot Sir!")
        elif "good night" in ask:
            say("Good night sir!")
            say("dont let the bed bugs bite") 
            break
        elif "activate youtube" in ask:
            SearchYT()
        elif "+" in ask:
            ask = ask.replace("+", "")
            try:
                plus_ans = "The Answer is" + str(int(ask[0]) + int(ask[3]))
                say(plus_ans)
            except Exception:
                say("Sorry, An Error Occured")
        elif "wikihow" in ask:
            ask = ask.replace("wikihow", "")
            say("Searching Wikihow")
            try:
                wikihow_ans = wh.search_wikihow(ask, 1)
                assert len(wikihow_ans) == 1
                wikihow_ans[0].print()
                say(wikihow_ans[0].summary)
                say("Did This Help you Sir!")
                did_help = takeCommand().lower()
                if "yes" in did_help:
                    say("That is Great to Hear sir!")
                elif "not at all" in did_help:
                    say("Sorry for Wasting your Time Sir!")
                elif "no" in did_help:
                    say("Sorry for Wasting your Time Sir!")
                elif "absolutely" in did_help:
                    say("Thanks a Lot Sir!!")
                else:
                    say("Okay Sir!")
            except:
                say("Some Error Occured")
        elif "hello" in ask:
            say("Hello Boss!")
        elif "hey" in ask:
            say("Hello Boss!")
        elif "which sid" in ask:
            say("I am Sid2")
        elif "number" in ask:
            ask = ask.replace("number", "")
            getNumber(ask.strip())
        elif "temperature" in ask:
            getTemp(ask)
        elif "today's date" in ask:
            getDate()
        elif "stack" in ask:
            SearchStackO()
        elif "open edge" in ask:
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif "open python" in ask:
            os.startfile("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Python\\Python310\\python.exe")
        elif "open google" in ask:
            openPage("https://www.google.com")      
        elif "open repo" in ask:
            openPage("https://github.com/The-Charged-Ion/SiD")
        elif "activate amazon" in ask:
            searchAmazon()
        elif "bing" in ask:
            ask = ask.replace('search bing', '')
            SearchBing(ask)
        elif "news headlines" in ask:
            getNews()
        elif "open github" in ask:
            openPage("https://www.github.com")
        elif "git" in ask:
            ask=ask.replace("github", "")
            say("Searching Github")
            try:
                say("Here are the Answers")
                openPage(f"https://www.github.com/search?q={ask}")
            except Exception:
                say("Some Erfror Occured While Processing")
        elif ask == "open":
            say("What should I Open sir!")
            try: 
                open_what = takeCommand().lower()
            except Exception:
                print("")
            if "python" in open_what:
                try:
                    os.startfile("C:\\Users\\Raman_b1j3bas\\AppData\\Local\\Programs\\Python\\Python310\\python.exe")
                except Exception:
                    say("Some Error Occured while Opening Python 3 dot 10 dot 4")
            elif "google" in open_what:
                try:
                    openPage("https://www.google.com")
                except Exception:
                    say("Some Error Occured while Opening google")
            elif "edge" in open_what:
                try:
                    os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                except Exception:
                    say("Some Error occured while Opening edge")
            elif "minecraft" in open_what:
                try:
                    os.startfile("C:\\Users\\rdgv\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
                except Exception:
                    say("Some Error occured while Opening minecraft")
            elif "command prompt" in open_what:
                try:
                    os.startfile("C:\\WINDOWS\\System32\\cmd.exe")
                except Exception:
                    say("Some Error occured while opening Command Prompt")
        elif "who is" in ask:
            WhoIs(ask)
        elif "sports update" in ask:
            getSportsNews()
        elif "technology update" in ask:
            getTechUpdate()
        elif "jarvis" in ask:
            say("Sir, My name is Sid not Jarvis!")
        elif "what happened" in ask:
            say("Nothing sir!")
        else:
            say("Sorry Sir! I Dont get That")
            continue

if __name__ == "__main__":
    WishMe()
    while True:
        try:
            permission = takeCommand().lower()
        except:
            continue
        if "wake up sid" in permission:
            ExecuteSid()
        elif "wake up" in permission:
            ExecuteSid()
        elif "goodbye" in permission:
            say("I am CLosing sir, Bye!")
            break
 



