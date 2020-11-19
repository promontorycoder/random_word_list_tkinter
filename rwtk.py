#! /usr/bin/env python3

from tkinter import *
import time
from string import digits
import  secrets


root = Tk()

root.geometry('800x400')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("Random Password String Generator")

Label(root, text = "Random Password String Generator", 
    font = 'arial 16 bold', bg='gray7', fg='lime green').pack()
    
Result1 = StringVar()
Result2 = StringVar()
Result3 = StringVar()
Result4 = StringVar()
Result5 = StringVar()
Result6 = StringVar()


def AllCallbacks():
    Callback1()
    Callback2()
    Callback3()
    Callback4()
    Callback5()
    Callback6()
    
def Callback1():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result1.set(str(pword[0].strip()))


def Callback2():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result2.set(str(pword[0].strip()))    


def Callback3():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result3.set(str(pword[0].strip()))


def Callback4():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result4.set(str(pword[0].strip()))


def Callback5():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result5.set(str(pword[0].strip()))


def Callback6():

    filename = 'only_words.txt'
    
    words = []
    pword = []
    
    with open(filename) as file_object:
        for line in file_object:
            words.append(line)
            
    pword.append(secrets.choice(words))
    
    Result6.set(str(pword[0].strip()))
    
    
def Callback7():
    new_file = str('new_pword_list.txt')
    
    date = time.strftime('%B %d, %Y')
    clock_time = time.strftime('%I:%M %p')
    phrase1 = ("                   'Random Passoword String Generator' \n" + 
        "                    Author: promontorycoder \n" + 
        "                    Author Email: promontorycoder@tutanota.com \n" +
        "                    GitHub: https://github.com/promontorycoder \n" +
        "\nPassphrase Words generated on ")
    phrase2 = " at "
        
    new_string = (Result1.get() + "\n" + Result2.get() + "\n" + Result3.get() + 
        "\n" + Result4.get() + "\n" + Result5.get() + "\n" + Result6.get())
        
    doc_write = (phrase1 + date + phrase2 + clock_time + "\n\n" + new_string)
    
    with open(new_file, 'w') as file_object:
        file_object.write(doc_write)

def Exit():
    exit()
    
E1 = Entry(root, font = 'arial 10', textvariable = Result1, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=55)    
B1 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback1).place(x=60, y=50)
    

E2 = Entry(root, font = 'arial 10', textvariable = Result2, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=85)    
B2 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback2).place(x=60, y=80)    


E3 = Entry(root, font = 'arial 10', textvariable = Result3, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=115)    
B3 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback3).place(x=60, y=110)


E4 = Entry(root, font = 'arial 10', textvariable = Result4, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=145)    
B4 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback4).place(x=60, y=140)


E5 = Entry(root, font = 'arial 10', textvariable = Result5, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=175)    
B5 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback5).place(x=60, y=170)


E6 = Entry(root, font = 'arial 10', textvariable = Result6, width=25, 
    bg= 'gray21', fg='lime green').place(x=300, y=205)    
B6 = Button(root, font = 'arial 10 bold', text = "Push to Generate a Random " +
    "word:", padx=2, bg='forest green', command = Callback6).place(x=60, y=200)


B7 = Button(root, font = 'arial 10 bold', text = 'EXIT', width=6, 
    command = Exit, bg = 'OrangeRed', padx=2, pady=1).place(x=60, y=350)    


B8 = Button(root, font = 'arial 10 bold', text = 'Generate All', width=25, 
    command = AllCallbacks, bg = 'forest green', padx=2).place(x=60, y=275)
    
B9 = Button(root, font = 'arial 10 bold', text = 'Print All', width=25,
    command = Callback7, bg = 'forest green', padx=2).place(x=300, y=275)
    
root.mainloop()

