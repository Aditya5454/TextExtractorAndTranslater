from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog
from googletrans import Translator 
from tkinter import messagebox
import pyttsx3
import os
#C:\Users\Aditya\AppData\Local\Programs\Tesseract-OCR

root = tk.Tk()
root.title('Language Translator')
root.geometry('900x500')



frame1 = Frame(root,width=600,height=370,relief = RIDGE,borderwidth=5,bg = 'white')
frame1.place(x=0 ,y=0)

Label(root,text="Language Translater",font = ("Helvetica 20 bold"),fg="black",bg = 'gray').pack(padx=20,pady=20)

def translate():
    long_1= text_entry1.get("1.0","end-1c")
    cl = choose_language.get()
    if long_1 == '':
        messagebox.showrror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0,'end')
        translator = Translator()
        output = translator.translate(long_1,dest=cl)
        text_entry2.insert('end',output.text)

def clear():
    text_entry1.delete(1.0,'end')
    text_entry2.delete(1.0,'end')

engine = pyttsx3.init()
def speaknow():
    text = text_entry1.get(1.0, END)
    gender = choose_gender.get()
    voices = engine.getProperty('voices')
    
    if(gender == 'MALE'):
        engine.setProperty('voice',voices[0].id)
        engine.say(text)
        engine.runAndWait()
    else:
        engine.setProperty('voice',voices[1].id)
        engine.say(text)
        engine.runAndWait()


a = tk.StringVar()

choose_gender = ttk.Combobox(frame1,width=27,textvariable=a, state='randomly',font=('verdana',10,'bold'))
choose_gender['values'] =(
    'MALE',
    'FEMAIL'
)
choose_gender.place(x=15,y=60)
choose_gender.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1,width=27,textvariable=l, state='randomly',font=('verdana',10,'bold'))
choose_language['values'] =(
                            'Afrikaans',
                            'Albanian',
                              'Arabic','Armenian',
                            'Azerbaijani',
                            'Basque', 'Belarusian',

'Bengali',

'Bosnian',

'Bulgarian',

'Catalan',

'Cebuano',

'Chichewa',

'Chinese',

'Corsican'

'Croatian',

'Czech',

'Danish',

'Dutch',

'English',

"Esperanto",
"Hindi",
"Telugu"
                        )


choose_language.place(x=305,y=60)
choose_language.current(0)
 


text_entry1 = Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
text_entry1.place(x=10,y=100)

text_entry2 = Text(frame1,width=20,height=7,borderwidth=5,relief=RIDGE,font=('verdana',15))
text_entry2.place(x=300,y=100)


btn1= Button(frame1,command=translate, text = "Translate",relief =RAISED, borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2',fg="white",cursor="hand2" )
btn1.place(x=185,y=300)

btn2= Button(frame1,command=clear, text = "Clear",relief =RAISED, borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2',fg="white",cursor="hand2" )
btn2.place(x=300,y=300)

btn3= Button(frame1,command=speaknow, text = "speech",relief ="sunken", borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2',fg="white",cursor="hand2" )
btn3.place(x=100,y=300)
#grid(row = 1, column = 3, pady = 10, padx = 100)


root.mainloop()



