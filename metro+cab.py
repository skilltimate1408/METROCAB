from tkinter import *
from tkinter import messagebox
a=Tk()
a.configure(bg="yellow")
lb1=Label(a,text="Ticket Booking",bg="Yellow",
          font=("Arial bold",25))
lb1.grid(column=1,row=0)
lb2=Label(a,text="From Station",bg="Yellow",
          font=("Arial bold",15))
lb2.grid(column=0,row=1)
lb3=Label(a,text="To Station",bg="Yellow",
          font=("Arial bold",15))
lb3.grid(column=0,row=2)
lb4=Label(a,text="Tickets",bg="Yellow",
          font=("Arial bold",15))
lb4.grid(column=0,row=3)
fs=["KPHB",
    "JNTUH",
    "MYP"]
click=StringVar()
click.set("Select")
d1=OptionMenu(a,click,*fs)
d1.grid(column=1,row=1)
ts=["KPHB",
    "JNTUH",
    "MYP"]
click2=StringVar()
click2.set("Select")
d2=OptionMenu(a,click2,*ts)
d2.grid(column=1,row=2)
tickets=[1,2,3,4,5]
click3=IntVar()
click3.set("Select")
d3=OptionMenu(a,click3,*tickets)
d3.grid(column=1,row=3)
lb5=Label(a,text="Do you need a cab?",bg="Yellow",
          font=("Arial bold",20))
lb5.grid(column=0,row=4)
def yes():
    lb6=Label(a,text="Cab Desitination",bg="Yellow",
          font=("Arial bold",15))
    lb6.grid(column=0,row=5)
    e1=Entry(a,width=15)
    e1.grid(column=1,row=5)
    def book():
        s1=click.get()
        s2=click2.get()
        cab=e1.get()
        t=int(click3.get())
        mbill=t*40
        cbill=150
        total=mbill+cbill
        messagebox.showinfo("","**Metro**from:"+s1+
                        "  To :"+s2+
                        "  Tickets :"+str(t)+
                        "  Bill : "+str(mbill)+
                        "\n **Cab** From: "+s2+
                        " To:  "+cab+
                        " cab bill : "+str(cbill)+
                         "\n Total : "+str(total))
    b=Button(a,text="Book",bg="Yellow",
          font=("Arial bold",15),command=book)
    b.grid(column=1,row=6)
b1=Button(a,text="Yes",bg="Yellow",
          font=("Arial bold",20),command=yes)
b1.grid(column=1,row=4)
def no():
    s1=click.get()
    s2=click2.get()
    t=int(click3.get())
    bill=t*40
    messagebox.showinfo("","from:"+s1+
                        "  To :"+s2+
                        "  Tickets :"+str(t)+
                        "  Bill : "+str(bill))
b2=Button(a,text="No",bg="Yellow",
          font=("Arial bold",20),command=no)
b2.grid(column=2,row=4)

a.mainloop()
