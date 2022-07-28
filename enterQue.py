from tkinter import *
import mysql.connector as ct
# from time import time, sleep


mydb = ct.connect(host="localhost", user="root", passwd="12345",database="hello")
mycursor = mydb.cursor()

def myconnect():
    mydb = ct.connect(host="localhost", user="root", passwd="12345",database="hello")
    return mydb

# def drop():
#     mycursor = mydb.cursor()
#     mycursor.execute(f"drop table test;")
#     drop(mydb)


def createtable():
    mycursor = mydb.cursor()
    # pass
    # mycursor.execute(f"drop table test;")
    # ob = drp()
    # ob.d()
    # mycursor.execute('''IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES 
    #              WHERE TABLE_SCHEMA = 'TheSchema' 
    #              AND  TABLE_NAME = 'TheTable'))''')
    mycursor.execute(f"DELETE FROM test;")
    # sleep(2)
    # print("in the create.........")
    # mycursor.execute(f"create table test (queno int primary key AUTO_INCREMENT, question varchar(300), \
    # optionA varchar(100), optionB varchar(100), optionC varchar(100), \
    # optionD varchar(100), ans varchar(5) );")
    # print("Previous Question removed")
    mydb.commit()

    # mycursor.execute(f'''insert into test values(1,"what is your name","Astha","Lovepreet","Ritika","Hardik","A");''')
    # mycursor.execute(f'''insert into test values(null,"what is your name","Astha","Lovepreet","Ritika","Hardik","A");''')
    # mycursor.execute(f"select * from test;")
    # mycursor.execute(f"describe table test ")

    # for i in mycursor:
    #     print(i)




def input():
    # input.count=2
    mycursor = mydb.cursor()
    def delete(): 
		#mycursor.execute(f'''insert into test values(null,"{myarg[0]}","{myarg[1]}","{myarg[2]}","{myarg[3]}","{myarg[4]}","{myarg[5]}");''')
        mycursor.execute(f'''insert into test values(null,"{nameentry.get()}","{A.get()}","{B.get()}","{C.get()}","{D.get()}","{answer.get()}");''')
		#mycursor.execute(f'''insert into test values(null,"{question.get()}","{optionA.get()}","{optionB.get()}","{optionC.get()}","{optionD.get()}","{ans.get()}");''')
        print("myques:",nameentry.get())
        print("Question added sucessfull ")
        # input.count=input.count+1
        mydb.commit()
        clear()

        # print(count.get())
        # frame.quit
        
    def clear():
        A.delete(0, END)
        B.delete(0, END)
        C.delete(0, END)
        D.delete(0, END)
        answer.delete(0, END)
        # que.delete(0, END)
        nameentry.delete(0, END)


    root = Tk()
    frame = Frame(root)

    frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
    frame.configure(relief=GROOVE)
    frame.configure(borderwidth="2")
    frame.configure(border="2")
    frame.configure(relief=GROOVE)
    frame.configure(background="#efefef")
    frame.configure(highlightbackground="#efefef")
    frame.configure(highlightcolor="black")
    frame.configure(width=925)
    
    root.geometry("744x444", )

    root.title('Create a Quiz')

    # count= StringVar()

    # print("Submitting form")

    #Text for our form
    # Q = Label(frame, text=f"Q{input.count}")
    Q = Label(frame, text=f"Ques", font="comicsansms 14 bold", pady=30)
    que = Label(root, text="Enter The Question", font="comicsansms 15 bold", pady=30)
    opA = Label(root, text="Option A", pady=10, font="7")
    opB = Label(root, text="Option B", pady=10, font="7")
    opC = Label(root, text="Option C", pady=10, font="7")
    opD = Label(root, text="Option D", pady=10, font="7")
    ansOp = Label(root, text="Choose the correct option(A, B, C, D)", font="13")

    #Pack text for our form
    frame.grid(row=1, column=1 )
    Q.grid(row=1, column=0)
    que.grid(row=1, column=1)
    opA.grid(row=2, column=1)
    opB.grid(row=3, column=1)
    opC.grid(row=4, column=1)
    opD.grid(row=5, column=1)
    ansOp.grid(row=12, column=1, pady=30)
    # Tkinter variable for storing entries
    question = StringVar()
    optionA = StringVar()
    optionB = StringVar()
    optionC = StringVar()
    optionD = StringVar()
    ans = StringVar()


    #Entries for our form
    nameentry = Entry(root, textvariable=question)
    A = Entry(root, textvariable=optionA)
    B = Entry(root, textvariable=optionB)
    C = Entry(root, textvariable=optionC)
    D = Entry(root, textvariable=optionD)
    answer = Entry(root, textvariable=ans)

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    nameentry.place(relx=0.42, rely=0.05,height=30, width=370)
    A.grid(row=2, column=3)
    A.place(relx=0.42, rely=0.13,height=30, width=250)
    B.grid(row=3, column=3)
    B.place(relx=0.42, rely=0.19,height=30, width=250)
    C.grid(row=4, column=3)
    C.place(relx=0.42, rely=0.25,height=30, width=250)
    D.grid(row=5, column=3)
    D.place(relx=0.42, rely=0.31,height=30, width=250)
    answer.grid(row=13, column=4)
    answer.place(relx=0.5, rely=0.44,height=30, width=80)


    #Button & packing it and assigning it a command
    bb = Button(root, text="Save & Enter New Question", font= 'comicsansms 12 bold' ,command=delete)
    bb.grid( row = 20, column= 7 )
    bb.place(relx=0.40, rely=0.65, height=50, width=250)
    
    root.mainloop()



# drop()
# createtable()
# input()


