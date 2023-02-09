import datetime
import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia



# hear The microphone and return the audio as text
def transform_audio_into_text():
    # store Recognizer in variable
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # wait time

        r.pause_threshold = 0.8

        # report that recording has begun
        print("Speak now")

        # saves what it hears as audio
        audio = r.listen(source)

        try:
            # search on Google
            request = r.recognize_google(audio, language="en-us", )

            # test om text
            print("you said " + request)

            # return request
            return request
        except sr.UnknownValueError:

            # show that it didn't understand audio
            print("me no understand")
            return "i am still waiting"

        # in case request cannot be resolved
        except sr.RequestError:

            # show that it didn't understand audio
            print("me no understand")
            return "i am still waiting"

        # any other errors
        except:
            # show that it didn't understand audio
            print("i no work")
            return "i am still waiting"


id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


def speak(message):
    # start engine  of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    # deliver message
    engine.say(message)
    engine.runAndWait()


def ask_day():
    # this will hold today's date.
    day = datetime.date.today()
    print(day)

    # this will tell us the day of the weel
    week_day = day.weekday()
    print(week_day)

    # names of  days
    calendar = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}
    speak(f"Today is {calendar[week_day]}")


# voice options

def ask_time():
    # variable with time info
    time = datetime.datetime.now()
    time = f" it is now {time.hour} hours {time.minute} minutes"

    speak(time)


def inital_greeting():
    # say greeting
    speak("Hello i am Ultron, how can i help you today? ")


# Brain of the assitant

def my_assistant():
    # first the assistant will greet the user
    inital_greeting()

    # used as a cut off variable
    go_on = True

    # main loop
    while go_on:

        # activate mic and save request
        my_request = transform_audio_into_text().lower()

        if "open youtube" in my_request:
            speak("Sure, i am opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "open browser" in my_request:
            speak("of course, i am on it")
            webbrowser.open("https://www.google.com")
            continue
        elif "what day is today" in my_request:
            ask_day()
            continue
        elif "what time is it" in my_request:
            ask_time()
            continue
        elif "wikipedia search for" in my_request:
            speak("i am looking for it")
            my_request = my_request.replace("wikipedia search for", "")
            answer = wikipedia.summary(my_request, sentences=1)
            speak("according to wikipedia: ")
            speak(answer)
            continue
        elif "search online for" in my_request:
            speak("i am looking for it")
            my_request = my_request.replace("search online for", "")
            pywhatkit.search(my_request)
            speak("this is what i found")
            continue
        elif "play" in my_request:
            speak("thats a great idea")
            pywhatkit.playonyt(my_request)
            continue
        elif "joke" in my_request:
            speak(pyjokes.get_joke())
            continue
        elif "goodbye" in my_request:
            speak("Ultron powering off")
            break
my_assistant()
