import pyttsx3
from tkinter import *
from gtts import gTTS
from playsound import playsound
import tkinter.messagebox as tmsg



# All Functions are Here ---------------------------------------------------------------
def chng_voice():
    file = word_Box.get()
    adio = pyttsx3.init()
    adio.setProperty('voice',1)
    adio.say(file)
    adio.runAndWait()

def es_lang():
    Message = word_Box.get()
    speech = gTTS(text = Message, lang='es')
    speech.save('data.mp3')
        

def fr_lang():
    Message = word_Box.get()
    speech = gTTS(text = Message, lang='fr')
    speech.save('data.mp3')
    

def pt_lang():
    Message = word_Box.get()
    speech = gTTS(text = Message, lang='pt')
    speech.save('data.mp3')
    

def default_lang():    
    Message = word_Box.get()
    speech = gTTS(text = Message, lang='en')
    speech.save('data.mp3')
    

def Text_to_speech():
    if Msg_field.get() == "":
        tmsg.showinfo('Error', 'you have to give a text!')
    else:
        playsound('data.mp3')
        
        


def exit():
    root.destroy()

def reset():
    Msg_field.set("")

# Making the Main Window ---------------------------------------------------------------
root = Tk()
root.geometry("644x432")
root.minsize(644, 432)
root.maxsize(644, 432)
root.title('Text To Speech')
root.configure(bg='#399FFF')

# All Variables are Here ----------------------------------------------------------------
Msg_field = StringVar()
radio = StringVar()
radio.set(RADIOBUTTON)


# Labels of the Application -------------------------------------------------------------
Label(root, text="  Text to Speech  ", font='sansarif 20 bold', bg='#399FFF', fg='black').pack()
Label(root, text=' Enter Your Text Here ', font='sansarif 17 bold', bg='#399fff',fg='black').place(x=200, y=60)

# Text Field ----------------------------------------------------------------------------
word_Box = Entry(root, textvariable = Msg_field, bg='#ffffff', width='40')
word_Box.place(x=200, y=107)

# Buttons of GUI ------------------------------------------------------------------------
Button(root, text=' Play Sound  ',font='ariel 11 bold', bg='#1D9E89', fg='#ffffff', command=Text_to_speech).place(x=200 ,y=135)
Button(root, text=' Reset Entry  ',font='ariel 11 bold', bg='#8D9EFF', command=reset).place(x=335 ,y=135)
Button(root, text=' Exit from Application  ',font='ariel 11 bold', bg='#FF777C',width=26, command=exit).place(x=200 ,y=185)

Label(root, text='Language Settings', font='ariel 13 bold', bg='#399fff').place(x=200, y=250)

# Language Radio buttons -----------------------------------------------------------------
Radiobutton(root, text='Spanish',variable=radio ,bg='#399FFF',font='ariel 10', value=1, command=es_lang).place(x=200, y=290)
Radiobutton(root, text='portuguese',variable=radio, bg='#399FFF', font='ariel 10', value=2, command=pt_lang).place(x=200, y=320)
Radiobutton(root, text='french',variable=radio ,bg='#399FFF', font='ariel 10', value=3, command=fr_lang).place(x=200, y=350)


Button(root, text='   Select  ', font='ariel  9', bg='#BEBED3', width=11).place(x=320, y=285)
Button(root, text='   Default  ', font='ariel  9', bg='#BEBED3', width=11, command=default_lang).place(x=320, y=315)
Button(root, text='Change Voice', font='ariel 9', bg='#BEBED3', command=chng_voice).place(x=320, y=345)


root.mainloop()
