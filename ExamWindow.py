from tkinter import *
# from typing import AnyStr
import mysql.connector as ct
mydb = ct.connect(host="localhost", user="root", passwd="12345",database="hello")
mycursor = mydb.cursor()



# mycursor.execute(f'''select * from test";''')
# for i in mycursor:
#     print(i)

# print(count,"TTTTTTTTTTTTTTT")
# show(c)
# count=c[0]





mycursor.execute(f"select * from test;")
global va # 
va = mycursor.fetchall()
va = va[0][0]
global count
count = va      # Question starting  from

global call
call = count  # to set que visit condition

global qno
qno = 0




mycursor.execute(f"select count(queno) from test;")
global val # Total no of question
val = mycursor.fetchone()
val = val[0]

global ms  #variable for marks
ms = 0

global ans
global corrans

def exam(rno):

    mydb = ct.connect(host="localhost", user="root", passwd="12345",database="hello")
    mycursor = mydb.cursor()

    
    root = Tk()
    root.title('Exam Window ')
    
    root.geometry("900x600")
    root.minsize(900,600)
    root.maxsize(900,600)
    
    f0 = Frame(root,bg="grey", borderwidth=2, relief=SUNKEN)
    f0.pack(side=TOP,fill="x")
    f1 = Frame(root,bg="red", borderwidth=7, relief=SUNKEN)
    f1.pack(side=RIGHT, fill="y")
    
 

    def show(mylist):

        
        # mycursor = mydb.cursor()
        # print(mylist)
        global corrans
        temp=0
        lst = mylist
        # print(type(lst))
        for i in lst:
            temp=temp+1
            if(temp==7):
                # print(i,"YYYYYYYYYYYYYYY")
                corrans = i
                break
                
        # print(corrans)
        def button():
            # pass
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            que.destroy()
            bt1.destroy()
            opAtxt.destroy()
            opBtxt.destroy()
            opCtxt.destroy()
            opDtxt.destroy()
            global count
            count = count +1
            # print(count)

            mydb = ct.connect(host="localhost", user="root", passwd="12345",database="hello")
            mycursor = mydb.cursor()

            if(ans==corrans):
                # print(corrans)
                global ms
                ms = ms+1
                mycursor = mydb.cursor()
                mycursor.execute(f'''UPDATE student SET marks={ms} WHERE rno={rno};''')
                # print(ms)
                mydb.commit()
            # print(val+call-1)
            if(count>=val+call):
                # print("fffffffffffffffff")
                ab = Label(f0,text="Exam is finished!!!", font="comicsansms 13 bold", pady=30)
                ab.pack()
                f1.destroy()
                root.configure(background='black')

                
            else:
                mycursor.execute(f'''select * from test where queno="{count}";''')
                j = mycursor.fetchone()
                show(j)



        #Text for our form
        q = Label(f1, text=f"                                              ")
        q.pack()
        global qno
        qno = qno+1
        que = Label(f0, text=f"Q{qno} {mylist[1]}", font="comicsansms 13 bold", padx=10, pady=30, background= "grey")
        que.pack(side=LEFT)
        # count=count+1
        # que.pack()
        # option text
        opAtxt = Label(root, text="Option A", font="comicsansms 10 bold")
        opAtxt.place(relx=0.25, rely=0.2)
        opBtxt = Label(root, text="Option B", font="comicsansms 10 bold")
        opBtxt.place(relx=0.25, rely=0.3)
        opCtxt = Label(root, text="Option C", font="comicsansms 10 bold")
        opCtxt.place(relx=0.25, rely=0.4)
        opDtxt = Label(root, text="Option D", font="comicsansms 10 bold")
        opDtxt.place(relx=0.25, rely=0.5)

        def update(val):
            global ans
            v.set(val)
            ans=v.get()

        v=StringVar()
        # v.set(None)
    
        b1 = Radiobutton(root,text=f"{mylist[2]}", variable=v,value="A",command=lambda: update("A"), padx=45, pady=30 )
        b1.pack()
        
        b2=Radiobutton(root,text=f"{mylist[3]}", variable=v,value="B",command=lambda: update("B"), padx=40, pady=10)
        b2.pack()
    
        b3=Radiobutton(root,text=f"{mylist[4]}", variable=v,value="C",command=lambda: update("C"), padx=45, pady=30)
        b3.pack()
    
        b4=Radiobutton(root,text=f"{mylist[5]}", variable=v,value="D",command=lambda: update("D"), padx=50, pady=10)
        b4.pack()


        # print(ans)

        #Button & packing it and assigning it a command
        bt1=Button(root,text="Save and Next",command=button, font="comicsansms 13 bold", padx=35, pady=15)
        bt1.place(relx=0.35, rely=0.62, width=150, height=35, bordermode='outside')
    
    # print(count,"_______________________")
    mycursor.execute(f'''select * from test where queno="{count}";''')
    j = mycursor.fetchone()
    show(j)
     
    
    # return 0
    root.mainloop()



exam(10)