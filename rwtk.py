#!/usr/bin/env python3


from tkinter import *
import time
from string import digits
import  secrets

# Create main tkinter window
root = Tk()
# Define main tkinter window parameters
root.geometry('800x500')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("Random Password String Generator")
# Create main tkinter window label
main_label = Label(root, 
    text = "Random Password String Generator", 
    font = 'arial 16 bold', 
    bg='gray7', 
    fg='lime green'
    )
# Place main_label on the main tkinter window
main_label.pack()

# Create variables for Stringvar(s)    
Result1 = StringVar()
Result2 = StringVar()
Result3 = StringVar()
Result4 = StringVar()
Result5 = StringVar()
Result6 = StringVar()

# Function to fill all tkinter entry boxes with separate random words
def AllCallbacks():
    Callback1()
    Callback2()
    Callback3()
    Callback4()
    Callback5()
    Callback6()

# Function to pick random word from list for populating first entry box    
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

    
# Function to print word list to file    
def print_all(filepath, filename):
    
    if len(entry_filepath.get()) == 0:
        tow.insert(END, "\nPlease enter a valid file path.")
        
    elif len(entry_filename.get()) == 0:
        tow.insert(END, "\nPlease enter a valid file name.")
        
    else:
        try:
            
            # Define file path and name for new password list
            new_file = (filepath + filename + '.txt')
            
            date = time.strftime('%B %d, %Y')
            clock_time = time.strftime('%I:%M %p')
            
            phrase1 = ("'Random Passoword String Generator'\n" + 
                "Author: promontorycoder \n" + 
                "Author Email: promontorycoder@tutanota.com \n" +
                "GitHub: https://github.com/promontorycoder \n" +
                "\nPassphrase Words generated on ")
            
            phrase2 = " at "
                
            new_string = (Result1.get() + "\n" + Result2.get() + "\n" + 
                Result3.get() + "\n" + Result4.get() + "\n" + Result5.get() + 
                "\n" + Result6.get())
                
            doc_write = (phrase1 + date + phrase2 + clock_time + "\n\n" + 
                new_string)
            
            with open(new_file, 'w') as file_object:
                file_object.write(doc_write)
                
            tow.insert(END, "\nYour list has been printed to file ...")
                
        except Exception as err:
            tow.insert(END, err)
                

# Function to clear text from tkinter text widget window
def clear_output():
    tow.delete(1.0, END)

   
# Function to exit program via exit button
def Exit():
    exit()


# Create tkinter text window widget
tow = Text(root,
    height=8,
    width=58,
    borderwidth=1,
    relief='ridge',
    bg='gray7',
    fg='red',
    )
    
# Place tkinter text widget on the root (main) window
tow.place(x=300, y=325)

# Create labels for filepath and filename entry boxes and output window
label_printing = Label(root, 
    text = "For printing list to .txt file, ", 
    font = 'arial 11', 
    bg='gray7', 
    fg='lime green'
    )
    
label_filepath = Label(root, 
    text = "Enter a file path: ", 
    font = 'arial 10', 
    bg='gray7', 
    fg='red'
    )
    
label_filename = Label(root, 
    text = "Enter a file name: ", 
    font = 'arial 10', 
    bg='gray7', 
    fg='red'
    )
    
label_output = Label(root, 
    text = "Text Output Window: ", 
    font = 'arial 11', 
    bg='gray7', 
    fg='red'
    )

label_printing.place(x=550, y=210)    
label_filepath.place(x=550, y=230)
label_filename.place(x=550, y=275)
label_output.place(x=300, y=300)

# Create tkinter entry boxes    
entry_word_one = Entry(root, 
    font = 'arial 10', 
    textvariable = Result1, 
    width=25, 
    bg= 'gray21', 
    fg='lime green'
    )

entry_word_two = Entry(root, 
    font = 'arial 10', 
    textvariable = Result2, 
    width=25,
    bg= 'gray21', 
    fg='lime green'
    )

entry_word_three = Entry(root, 
    font = 'arial 10', 
    textvariable = Result3, 
    width=25, 
    bg= 'gray21', 
    fg='lime green'
    )

entry_word_four = Entry(root, 
    font = 'arial 10', 
    textvariable = Result4, 
    width=25, 
    bg= 'gray21', 
    fg='lime green'
    )

entry_word_five = Entry(root, 
    font = 'arial 10', 
    textvariable = Result5, 
    width=25, 
    bg= 'gray21', 
    fg='lime green',
    )

entry_word_six = Entry(root, 
    font = 'arial 10', 
    textvariable = Result6, 
    width=25, 
    bg= 'gray21', 
    fg='lime green'
    )
    
entry_filepath = Entry(root, 
    font = 'arial 10',
    width = 25,
    bg='gray21',
    fg='lime green',
    )
    
entry_filename = Entry(root, 
    font = 'arial 10',
    width = 25,
    bg='gray21',
    fg='lime green',
    )

# Place tkinter entry boxes in the main window
entry_word_one.place(x=300, y=55)
entry_word_two.place(x=300, y=85)
entry_word_three.place(x=300, y=115)
entry_word_four.place(x=300, y=145)
entry_word_five.place(x=300, y=175)
entry_word_six.place(x=300, y=205)
entry_filepath.place(x=550, y=250)
entry_filename.place(x=550, y=295)      

# Create tkinter function buttons    
btn_word_one = Button(root,
    command = Callback1,
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    bg='forest green', 
    padx=2, 
    )

btn_word_two = Button(root, 
    command = Callback2,
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    bg='forest green', 
    padx=2, 
    )

btn_word_three = Button(root, 
    command = Callback3,
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    padx=2, 
    bg='forest green', 
    )

btn_word_four = Button(root, 
    command = Callback4, 
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    padx=2, 
    bg='forest green', 
    )

btn_word_five = Button(root, 
    command = Callback5,
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    padx=2, 
    bg='forest green', 
    )

btn_word_six = Button(root, 
    command = Callback6, 
    text = "Push to Generate a Random word:", 
    font = 'arial 10 bold', 
    padx=2, 
    bg='forest green', 
    )

btn_exit = Button(root, 
    command = Exit, 
    text = 'EXIT', 
    font = 'arial 10 bold', 
    width=6, 
    bg = 'OrangeRed', 
    padx=2, 
    pady=1
    )

btn_generate_all = Button(root, 
    command = AllCallbacks, 
    text = 'Generate All', 
    font = 'arial 10 bold', 
    width=25, 
    bg = 'gray7',
    fg='lime green', 
    padx=2,
    )

btn_print_all = Button(root, 
    command = lambda: print_all(entry_filepath.get(), entry_filename.get()), 
    text = 'Print All', 
    font = 'arial 10 bold', 
    width=25,
    bg = 'gray7',
    fg='lime green', 
    padx=2,
    )
    
btn_clear_output = Button(root, 
    command = clear_output, 
    text = 'Clear Output', 
    font = 'arial 8', 
    bg = 'royal blue',
    fg='lime green', 
    padx=2,
    )

# Place tkinter function buttons in the main window
btn_word_one.place(x=60, y=50)
btn_word_two.place(x=60, y=80)
btn_word_three.place(x=60, y=110)
btn_word_four.place(x=60, y=140)
btn_word_five.place(x=60, y=170)
btn_word_six.place(x=60, y=200)
btn_exit.place(x=40, y=450)
btn_generate_all.place(x=60, y=250)
btn_print_all.place(x=300, y=250)
btn_clear_output.place(x=210, y=375) 
    
    
root.mainloop()
