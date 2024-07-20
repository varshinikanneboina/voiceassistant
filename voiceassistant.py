import speech_recognition as sr# To convert speech into text
import pyttsx3  # To convert text into speech
import datetime  # To get the date and time
import wikipedia  # To get information from wikipedia
import webbrowser  # To open websites
import os  # To open files
import time  # To calculate time
import subprocess  # To open files
from tkinter import *  # For the graphics
import pyjokes  # For jokes
name_assistant = "Hello Assistant"  # The name of the assistant
screen = Tk()
name_label = Label()
microphone_button = Button()
settings_button = Button()
info_button = Button()
settings_counter = 0
info_counter = 0
info_str = '''The basic voice assistant can be used to perform trivial, day-to-day tasks and uses speech recognition to interpret the user's voice commands.
The user can ask questions, control music playback, search the web, etc. using the voice assistant.
The voice assistant also responds back to the user using a synthesized voice.'''
# 'sapi5' is the argument you have to use for windows, I am not sure what it is for Mac and Linux
engine = pyttsx3.init('sapi5')
voice_speed = 150
engine.setProperty('rate', voice_speed)
voices = engine.getProperty('voices')  # To get the voice
engine.setProperty('voice', voices[1].id)  # defines the gender of the voice.
def speak(text):
    engine.say(text)
    print(name_assistant + " : " + text)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
    elif hour >= 12 and hour < 18:  # This uses the 24 hour system so 18 is actually 6 p.m
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th',
                    '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    speak("Today is " + month_names[month_name-1] +
          " " + ordinalnames[day_name-1] + '.')
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
def wikipedia_screen(text):
    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    message = Message(wikipedia_screen, text=text)
    message.pack()
def get_audio():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Started Listening.")
        audio = r.listen(source, phrase_time_limit=3)
        print("Stopped Listening.")
    try:
        text = r.recognize_google(audio, language='en-US')
        print('You: ' + ': ' + text)
        return text
    except:
        return "None"
def Process_audio():
    run = 1
    if __name__ == '__main__':
        while run == 1:
            statement = get_audio().lower()
            results = ''
            run += 1
            if "hello" in statement or "hi" in statement:
                wishMe()
            if "good bye" in statement or "bye" in statement or "stop" in statement:
                speak('Your personal assistant ' +
                      name_assistant + ' is shutting down, Good bye')
                screen.destroy()
                break
            if 'wikipedia' in statement:
                try:
                    speak('Searching Wikipedia...')
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=3)
                    speak("According to Wikipedia")
                    wikipedia_screen(results)
                except:
                    speak("Error")
            if 'joke' in statement:
                speak(pyjokes.get_joke())
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube opening now")
                time.sleep(5)
            if 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google opening now")
                time.sleep(5)
            if 'open gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("Google Mail opening now")
                time.sleep(5)
            if 'open netflix' in statement:
               webbrowser.open_new_tab("https://www.netflix.com/browse")
               speak("Netflix opening now")

            if 'open prime video' in statement:
                webbrowser.open_new_tab("https://www.primevideo.com")
                speak("Amazon Prime Video opening now")
                time.sleep(5)
            if 'news' in statement:
                news = webbrowser.open_new_tab(
                    "https://timesofindia.indiatimes.com")
                speak('Here are some headlines from Times of India, Happy reading')
                time.sleep(6)
            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)
            if 'corona' in statement:
                news = webbrowser.open_new_tab(
                    "https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)
            if 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            if 'date' in statement:
                date()
            if 'who are you' in statement or 'what can you do' in statement:
                speak('I am '+name_assistant+' your personal assistant. I am programmed for minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra')
            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Batch Five.")
            if 'note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)
            if 'note this' in statement:
                statement = statement.replace("note this", "")
                note(statement)
            speak(results)
# For preventing multiple settings Toplevel widgets
def reset_settings_counter(event):
    global settings_counter
    settings_counter = 0

# For preventing multiple info Toplevel widgets
def reset_info_counter(event):
    global info_counter
    info_counter = 0
def info():
    global info_str, info_counter
    if info_counter == 0:
        info_counter = 1
        info_screen = Toplevel(screen)
        info_screen.title("Info")
        info_screen.bind('<Destroy>', reset_info_counter)
        creator_label = Label(info_screen, text=info_str)
        creator_label.pack()
        for_label = Label(info_screen, text="- team 12")
        for_label.pack()
id_var = IntVar()  # For changing assistant voice
theme_var = IntVar()  # For the Theme
def change_assistant_voice():
    t = id_var.get() - 1
    engine.setProperty('voice', voices[t].id)

def change_theme():
    if theme_var.get() == 1:
        screen.configure(bg='white')
        name_label.configure(bg='black', fg='white')
        microphone_button.configure(bg='white')
        settings_button.configure(bg='white')
        info_button.configure(bg='white')
    elif theme_var.get() == 2:
        screen.configure(bg='black')
        name_label.configure(bg='grey', fg='black')
        microphone_button.configure(bg='black')
        settings_button.configure(bg='black')
        info_button.configure(bg='black')
def settings():
    global settings_counter
    if settings_counter == 0:
        settings_counter = 1
        settings_screen = Toplevel(screen, background='white')
        settings_screen.title('Settings')
        settings_screen.geometry('200x200')
        settings_screen.bind('<Destroy>', reset_settings_counter)
        voice_label = Label(settings_screen, text='Assistant Voice Selection', background='black', foreground='white', font=("Calibri", 13))
        voice_label.pack()
        male_voice_choice = Radiobutton(settings_screen, text='Male', variable=id_var, value=1, command=change_assistant_voice, background='white')
        male_voice_choice.pack()
        female_voice_choice = Radiobutton(settings_screen, text='Female', variable=id_var, value=2, command=change_assistant_voice, background='white')
        female_voice_choice.pack()
        theme_label = Label(settings_screen, text='Theme Selection', background='black', foreground='white', font=("Calibri", 13))
        theme_label.pack()
        light_theme = Radiobutton(settings_screen, text='Light', variable=theme_var, value=1, command=change_theme, background='white')
        light_theme.pack()
        dark_theme = Radiobutton(settings_screen, text='Dark', variable=theme_var, value=2, command=change_theme, background='white')
        dark_theme.pack()
        settings_screen.mainloop()

def main_screen():
    global screen
    global name_label
    global microphone_button
    global settings_button
    global info_button
    screen.title(name_assistant)
    screen.geometry("750x750")
    screen.configure(bg='white')
    screen.resizable(1, 1)
    img1 = PhotoImage(file='microphone.png')
    img2 = PhotoImage(file='settings1.png')
    img3 = PhotoImage(file='info.png')
    name_label = Label(screen, text=name_assistant, width=500,bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()
    microphone_button = Button(image=img1, command=Process_audio, borderwidth=0, bg='white',width=300,height=300)
    microphone_button.pack(pady=0)
    settings_button = Button(image=img2, borderwidth=0,bg='white', command=settings,width=200, height=200)
    settings_button.pack(pady=15)
    info_button = Button(image=img3, command=info, bg='white', borderwidth=0,width=150, height=150)
    info_button.pack(pady=15)
    screen.mainloop()
main_screen()  # Driver Call
