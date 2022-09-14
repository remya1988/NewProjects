from tkinter import *
window = Tk()
window.title("New Window Demo")
window.geometry("500x300")

def getVal():
    print("Values are accepted......")
Label(window, text="Registration Form", font ="ar 15 bold").grid(row=0,column=3)
name=Label(window,text="Name")
email=Label(window,text="email")
phone=Label(window,text="phone")

name.grid(row=1,column=2)
email.grid(row=2,column=2)
phone.grid(row=3,column=2)

namevalue = StringVar
emailvalue = StringVar
phonevalue = StringVar
chkvalue = StringVar

nameentry=Entry(window,textvariable=namevalue)
emailentry=Entry(window,textvariable=emailvalue)
phoneentry=Entry(window,textvariable=phonevalue)

nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)

chkbtn = Checkbutton(text="Remember me?",variable=chkvalue)
chkbtn.grid(row=4,column=3)

Button(text="Submit",command=getVal).grid(row=5,column=3)

window.mainloop()