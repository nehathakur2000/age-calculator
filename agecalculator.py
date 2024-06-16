from tkinter import *
from datetime import date

root=Tk()

def calculateAge():
    today = date.today()
    birthDate = date(int(e_year.get()), int(e_month.get()), int(e_day.get()))

    # calculating age by subtracting birthdate from today's date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    
    # creating a Label widget to show the calculated age using 
    # grid method
    lbl1=Label(frame,text=f"{e_name.get()} your age is {age}",font="arial 15 bold")
    lbl1.place(x=180,y=350)



frame= Frame(root,widt=500,height=400,bg="pink")
frame.place(x=400,y=80)

l_title= Label(frame,text="Age Calculator",font="arial 20 bold",bg="black",fg="white")
l_title.place(x=200,y=30)

l_name= Label(frame,text="Name:", font="arial 12 bold ")
l_name.place(x=60,y=90)

e_name=Entry(frame,font="arial 12 bold")
e_name.place(x=190,y=90)

l_year= Label(frame,text=" Year:", font="arial 12 bold ")
l_year.place(x=60,y=140)
e_year=Entry(frame,font="arial 12 bold")
e_year.place(x=190,y=140)

l_month= Label(frame,text=" Month:", font="arial 12 bold ")
l_month.place(x=60,y=180)
e_month=Entry(frame,font="arial 12 bold")
e_month.place(x=190,y=180)

l_day= Label(frame,text=" Date:", font="arial 12 bold ")
l_day.place(x=60,y=230)
e_day=Entry(frame,font="arial 12 bold")
e_day.place(x=190,y=230)

# nameValue=StringVar()
# yearValue=StringVar()
# monthValue=StringVar()
# dayValue=StringVar()

btn1=Button(frame,text="Calculate Age",font="arial 12 bold",padx=10,pady=6,background="black",fg="white",command=calculateAge)
btn1.place(x=200,y=270)

mainloop()