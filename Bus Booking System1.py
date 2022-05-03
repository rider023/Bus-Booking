from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk,Image
import sqlite3
import splash

def Second_Page():
    sec = Toplevel(root)
    sec.title("Add Bus")
    sec.geometry('500x600')
    Full_Name=StringVar()
    Contact_No=StringVar()
    Address=StringVar()
    Operator=StringVar()
    Bus_Type=StringVar()
    From_p=StringVar()
    To_p=StringVar()
    Date=StringVar()
    Dep_Time=StringVar()
    Arrival_Time=StringVar()
    Fair=IntVar()
    Seats=IntVar()
    
    def busdetail():
        name=Full_Name.get()
        contact=Contact_No.get()
        address =Address.get()
        operator=Operator.get()
        bus_type=Bus_Type.get()
        fr=From_p.get()
        t=To_p.get()
        date=Date.get()
        dep_time = Dep_Time.get()
        arr_time = Arrival_Time.get()
        fair = Fair.get()
        seats = Seats.get()
    
        conn = sqlite3.connect("busdetails.db")
        with conn:
             cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS BUSDETAIL(Full_Name text,Contact_No int,Address varchar,Operator text,Bus_Type text,From_p text,To_p text,Date varchar,Dep_Time varchar,Arrival_Time varchar,Fair int,Seats int)")
        cursor.execute('INSERT INTO BUSDETAIL(Full_Name,Contact_No,Address,Operator,Bus_Type,From_p,To_p,Date,Dep_Time,Arrival_Time,Fair,Seats) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(name,contact,address,operator,bus_type,fr,t,date,dep_time,arr_time,fair,seats))
        conn.commit() 
        tkinter.messagebox.showinfo("Detail","Detail Saved")
        sec.destroy()
    frame13 =Label(sec,text="Add Bus Details",font=("Times New Roman",25),fg="#000000").place(x=150,y=40)
    frame3 =Label(sec,text="Full Name",font=("Times New Roman",13),fg="#000000").place(x=60,y=80)

    entry1=Entry(sec,textvar=Full_Name,font =("Times New Roman",12),bg ="light grey")
    entry1.place(x=170,y=80,width=250,height=25)

    frame4 =Label(sec,text="Contact No.",font=("Times New Roman",13),fg="#000000").place(x=60,y=120)

    entry2=Entry(sec,textvar=Contact_No,font =("Times New Roman",12),bg ="light grey")
    entry2.place(x=170,y=120,width=250,height=25)

    frame5 =Label(sec,text="Address",font=("Times New Roman",13),fg="#000000").place(x=60,y=160)

    entry3=Entry(sec,textvar=Address,font =("Times New Roman",12),bg ="light grey")
    entry3.place(x=170,y=160,width=250,height=25)
    def onclick():
        frame6 =Label(sec,text="Operator",font=("Times New Roman",13),fg="#000000").place(x=60,y=240)

        entry4=Entry(sec,textvar=Operator,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=240,width=250,height=25)

        frame6 =Label(sec,text="Bus Type",font=("Times New Roman",13),fg="#000000").place(x=60,y=280)

        entry4=Entry(sec,textvar=Bus_Type,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=280,width=250,height=25)

        frame6 =Label(sec,text="From",font=("Times New Roman",13),fg="#000000").place(x=60,y=320)

        entry4=Entry(sec,textvar=From_p,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=320,width=250,height=25)

        frame6 =Label(sec,text="To",font=("Times New Roman",13),fg="#000000").place(x=60,y=360)

        entry4=Entry(sec,textvar=To_p,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=360,width=250,height=25)

        frame6 =Label(sec,text="Date",font=("Times New Roman",13),fg="#000000").place(x=60,y=400)

        entry4=Entry(sec,textvar=Date,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=400,width=250,height=25)

        frame6 =Label(sec,text="Dep Time",font=("Times New Roman",13),fg="#000000").place(x=60,y=440)

        entry4=Entry(sec,textvar=Dep_Time,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=440,width=250,height=25)

        frame6 =Label(sec,text="Arrival Time",font=("Times New Roman",13),fg="#000000").place(x=60,y=480)

        entry4=Entry(sec,textvar=Arrival_Time,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=480,width=250,height=25)

        frame6 =Label(sec,text="Fair",font=("Times New Roman",13),fg="#000000").place(x=60,y=520)

        entry4=Entry(sec,textvar=Fair,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=520,width=250,height=25)
        
        frame6 =Label(sec,text="Seats",font=("Times New Roman",13),fg="#000000").place(x=60,y=560)

        entry4=Entry(sec,textvar=Seats,font =("Times New Roman",12),bg ="light grey")
        entry4.place(x=170,y=560,width=250,height=25)
                
    button= Button(sec,command = onclick,text = "Add Details",cursor="hand2",bg="#f6d7ab",font=("Times New Roman",10)).place(x=250,y=200)
    button= Button(sec,command = busdetail,text = "Save",cursor="hand2",bg="#f6d7ab",font=("Times New Roman",10)).place(x=10,y=200)       

def Third_page():
    #root.destroy()
    book = Toplevel(root)
    book.title("Bus Boooking")
    book.configure(background='brown')
    book.geometry('900x500')

    frame12 =Label(book,text="Book Your Bus",font=("Times New Roman",25),fg="#000000").place(x=340,y=100)
    From_p=StringVar()
    To_p=StringVar()
    Date=StringVar()
    Bus_Type=StringVar()
    framea =Label(book,text="From",font=("Times New Roman",13),fg="#000000").place(x=100,y=200)

    entrya=Entry(book,font =("Times New Roman",12),bg ="light grey",textvar = From_p)
    entrya.place(x=170,y=200,width=150,height=25)
    
    frameb =Label(book,text="To",font=("Times New Roman",13),fg="#000000").place(x=345,y=200)

    entryb=Entry(book,font =("Times New Roman",12),bg ="light grey", textvar = To_p)
    entryb.place(x=390,y=200,width=150,height=25)

    framec =Label(book,text="Date",font=("Times New Roman",13),fg="#000000").place(x=560,y=200)

    entryc=Entry(book,font =("Times New Roman",12),bg ="light grey")
    entryc.place(x=610,y=200,width=100,height=25)
    
    framed =Label(book,text="Bus Type",font=("Times New Roman",13),fg="#000000").place(x=400,y=250)
    clicked = StringVar()
    clicked.set("AC")
    bustype = OptionMenu(book,clicked,"AC","Non AC","Sleeper","Seater").place(x=480,y=250)

    def update():
        choice=IntVar()
        #seatsbook=IntVar()
        print(seat)
        conn = sqlite3.connect("busdetails.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute('UPDATE BUSDETAIL SET Seats = Seats - ? WHERE Contact_No = ?',(seat, ID))
        conn.commit()
        tkinter.messagebox.showinfo("showinfo", "Your Seat Booked Successfully")
        
    
    
    def search_bus():
        global ID
        choice=IntVar()
        seatsbook=IntVar()
        s=Toplevel(root)
        s.geometry('900x500')

                
        
        #From_p=StringVar()
        #To_p=StringVar()
        #Date=StringVar()
        


        fr=From_p.get()
        t=To_p.get()
        #date=Date.get()
        #bus_type=Bus_Type.get()
        conn = sqlite3.connect("busdetails.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute("SELECT * from BUSDETAIL WHERE From_p = ? AND To_p = ? ",(fr,t))
        r = cursor.fetchall()
        d = len(r)
        L = Label(s, text = "Operator,Bus_Type,From_p,To_p,Date,Dep_Time,Arrival_Time,Fair,Seats,TYPE AC=1:NON AC = 0", font = ('Constantia',10)).place(x = 100, y = 160)
        i = 0
        for i in range(0,d):
            str = " BUS %s" % (r[i],)
            Radiobutton(s, text = str,value = i,font = ('constantia', 10), variable = choice).place(x = 100, y = 200+100*i)
            i = i + 1
        ID = r[choice.get()][1]   
                
        label = Label(s, text="No of Seats you want = ", font = ('Times New Roman', 20)).place(x = 300, y = 100)
        entry = Entry(s, textvar = seatsbook).place(x = 700, y = 100)
        global seat 
        seat = seatsbook.get()
        button= Button(s, text = 'book', font = ('Constantia', 20),command = update).place(x = 100, y = 100)
        conn.commit()
        
       
    button= Button(book,command=search_bus,text = "Search",cursor="hand2",bg="#f6d7ab",font=("Times New Roman",10)).place(x=750,y=200,width=70)

root = Tk()
frame=Frame(root, bg="#f6d7ab")
frame.place(x=290,y=150,height=250,width=350)

frame1 =Label(frame,text="Bus Booking Service",font=("Coolvetica",13,"bold"),fg="#806032", bg="#f6d7ab").place(x=60,y=10)
frame2 =Label(frame,text="Login Here",font=("Long Shot",30,"bold"),fg="#806032", bg="#f6d7ab").place(x=60,y=30)

frame3 =Label(frame,text="Username",font=("Times New Roman",13),fg="#000000", bg="#f6d7ab").place(x=60,y=80)

entry1=Entry(frame,font =("Times New Roman",14),bg ="light grey")
entry1.place(x=60,y=110,width=250,height=25)


frame4 =Label(frame,text="Password",font=("Times New Roman",13),fg="#000000", bg="#f6d7ab").place(x=60,y=140)

entry2=Entry(frame,font =("Times New Roman",14),bg ="light grey")
entry2.place(x=60,y=170,width=250,height=25)

username = StringVar()
password = StringVar()
def first_page():
    
    #user=username.get()
    #pas=password.get()
    #frame3.focus()

    #if (user==str(1234) and pas==str(2345)):
    top=Toplevel(root)
    top.title("Bus Services")
    top.geometry('900x500')
    top.configure(background='brown')
    label1 = Label(top,text="Bus Booking Service",font=("Coolvetica",30,"bold"),fg="#806032").place(x=250,y=20)
    #***********IMAGE SPACE****************
    img = Image.open("BUS-BOOKING.png")
    re_img = img.resize((300,200))
    img = ImageTk.PhotoImage(re_img)
    Label(top,image = img).place(x=300,y=150)
    add_bus= Button(top,command = Second_Page,text="Add Bus",cursor="hand2",bg="#f6d7ab",font=("Times New Roman",10)).place(x=100,y=400)
    Book_bus= Button(top,command =Third_page,text="Book Bus",cursor="hand2",bg="#f6d7ab",font=("Times New Roman",10)).place(x=700,y=400)
    #else:
        #tkinter.messagebox.askyesno("Bus Booking System","You have entered wrong details")
        #username.set("")
        #pas=password.set("")
lb_signin= Button(root,command=first_page,cursor="hand2",text="SignIn",fg="white",bg="#806032",font=("Times New Roman",12)).place(x=500,y=365,width=100, height=30)


        
fp= Button(frame,text="Forget Password",cursor="hand2",fg="red",bg="#f6d7ab",bd=0,font=("Times New Roman",10)).place(x=59,y=195)

        


root.title("Bus Booking Service")
root.geometry("900x500")
root.configure(background='brown')
root.mainloop()






