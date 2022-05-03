from tkinter import *
root=Tk()
root.title("Introduction")
root.geometry('900x500')
Label(root,text="Project Title: Bus Booking System",font=("Times New Roman",18),fg="Black").place(x=280,y=80)
Label(root,text="Developed as part of the course Advanced Programming Lab & DBMS",font=("Times New Roman",18),fg="Black").place(x=100,y=140)
Label(root,text="Developed By Shivang Srivastava,191b232,6388214681,shivangs300@gmail.com",font=("Times New Roman",13),fg="Blue").place(x=140,y=200)
Label(root,text="---------------------------",font=("Times New Roman",18),fg="Blue").place(x=310,y=240)
Label(root,text="Project Supervisors : Dr. Mahesh Kumar Singh & Nilesh Patel",font=("Times New Roman",13),fg="Brown").place(x=220,y=280)
Label(root,text="Make Mouse Movement Over this Screen to close",font=("Times New Roman",13),fg="Green").place(x=260,y=320)

#root.configure(background='brown')






def close(e=2):
    root.destroy()

root.bind('<Motion>', close)

root.mainloop()
