from tkinter import *
from tkinter import ttk
from tkinter import font
from enterQue import *
# from deleteAndCreate import deleteAndCrt
from deleteAndCreate import *
from credential import *
from Result import *



import tkinter
root = Tk()

frame = Frame(root)
frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
frame.configure(relief=GROOVE)
frame.configure(borderwidth="2")
frame.configure(border="2")
frame.configure(background="#efefef")
frame.configure(highlightbackground="#efefef")
frame.configure(highlightcolor="black")
frame.configure(width=925)


def teacher():
    # pass
    # frame.quit
    deleteAndCrt()
    # tecr()

def credential():
    # pass
    credentialInput()

def res():
    # pass
    result()

def showmain():

    root.title('Main Window ')

    root.geometry("700x700")

    f0 = Frame(root,bg="grey", borderwidth=2, relief=SUNKEN)
    f0.grid(row=2, column=2)
    f1 = Frame(root,bg="White", borderwidth=7, relief=SUNKEN)
    f1.grid(row=3, column=2)
    value=StringVar()



    lbl = ttk.Label(root, text="Select Your Identity ", font="comicsansms 13 bold", padding='10', background="#efefef")
    lbl.place(relx=0.05, rely=0.15, width=300, height=45, bordermode='outside')
    
    lb2 = ttk.Label(root, text="Check The Result ", font="comicsansms 13 bold", padding='10', background="#efefef")
    lb2.place(relx=0.05, rely=0.45, width=300, height=45, bordermode='outside')
    

    b2=tkinter.Button(text="Teacher",command=teacher, font="comicsansms 13 bold")
    b3=tkinter.Button(text="Student",command=credential, font="comicsansms 13 bold")
    b1=tkinter.Button(text="Check Result",command=res, font="comicsansms 13 bold")
    b2.place(relx=0.35, rely=0.25, width=150, height=35, bordermode='outside')
    b3.place(relx=0.35, rely=0.35, width=150, height=35, bordermode='outside')
    b1.place(relx=0.35, rely=0.55, width=150, height=35, bordermode='outside')

    root.mainloop()

showmain()