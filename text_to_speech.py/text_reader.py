# import gtts
# import playsound

# text = input("enter text to read: ")
# sound = gtts.gTTS(text, lang="hi")

# sound.save("snd.mp3")
# playsound.playsound("snd.mp3")


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root = Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.geometry("900x450+200+100")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    text=text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text=text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if(text):
        if(speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()




# icon
image_icon = PhotoImage(file="img\speaking.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)


logo = PhotoImage(file="img/Mic3.png")
Label(Top_frame, image=logo, bg="white").place(x=20, y=15) 

Label(Top_frame, text="Text To Speech", font="arial 20 bold", bg="white", fg="black").place(x=60, y=30) 


###########

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=140, width=500, height=250)

Label(root, text="Voice", font="aria; 15 bold", bg="#305065", fg="white").place(x=580,y=165)
Label(root, text="Speed", font="aria; 15 bold", bg="#305065", fg="white").place(x=760,y=165)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imageicon = PhotoImage(file="img/speaking1.png")
btn=Button(root, text="Speak", compound=LEFT, image=imageicon, width=130, height=50, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="img/save.png")
save=Button(root, text="save", compound=LEFT, image=imageicon2, width=130, height=50, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=730, y=280)




root.mainloop()