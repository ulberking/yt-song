from tkinter import *
from tkinter.ttk import *
import requests
import pywhatkit
root = Tk()
root.title('Online Music')
root.geometry('500x300')

def listensong():
    song=song_name.get()
    pywhatkit.playonyt(song)

label = Label(root,text='Enter your song',font=('bold',15))
label.place(x=170,y=30)
song_name=StringVar()
song_entry = Entry(root, textvariable=song_name)
song_entry.place(x=170,y=60)
search = Button(root,text='Search',width=12,command=listensong)
search.place(x=185,y=90)
root.mainloop()
