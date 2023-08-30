from tkinter import font
import googletrans
from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox

root = Tk()
root.title("Language Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="cyan")

def translate():
    content = content1.get(1.0, END)
    c1 = Translator()
    trans_content = c1.translate(text= content, src = combo1.get(), dest = combo2.get())
    trans_content = trans_content.text
    content2.delete(1.0, END)
    content2.insert(END, trans_content)

def clear():
    content1.delete(1.0, END)
    content2.delete(1.0, END)

language = googletrans.LANGUAGES
language_list = list(language.values())
lang = language.keys()

combo1 = AutocompleteCombobox(root, completevalues = language_list, font = ("Arial", 15))
combo1.place(x=110, y=20)
combo1.set("english")

combo2 = AutocompleteCombobox(root, completevalues = language_list, font = ("Arial", 15))
combo2.place(x=730, y=20)
combo2.set("choose language")

f = Frame(root, bg="Black", bd=5)
f.place(x=20, y=80, width=440, height=210)

content1 = Text(f, font=("Arial", 15), bg="White")
content1.place(x=0, y=0, width=430, height=200)
scroll1 = Scrollbar(f)
scroll1.pack(side="right", fill="y")
scroll1.configure(command=content1.yview)
content1.configure(yscrollcommand=scroll1.set)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=80, width=440, height=210)

content2 = Text(f1, font=("Arial", 15), bg="White")
content2.place(x=0, y=0, width=430, height=200)
scroll2 = Scrollbar(f1)
scroll2.pack(side="right", fill="y")
scroll2.configure(command=content2.yview)
content2.configure(yscrollcommand=scroll2.set)

trans = Button(root, text="Translate Text", font=("Arial", 15, "bold"), bg="teal", fg="white", width=20, height=2, command= translate)
trans.place(x=260, y=310)

trans = Button(root, text="Clear", font=("Arial", 15, "bold"), bg="teal", fg="white", width=20, height=2, command= clear)
trans.place(x=575, y=310)

root.mainloop()