from tkinter import *
from datetime import *


root = Tk()
root.geometry("700x500")
root.title("age calculator")

photo = PhotoImage(file="/sdcard/python_projects/tkinter_proj/calc.png")
myimage = Label(image = photo)
myimage.grid(row=0,column=1)

def calculateage():
	today = date.today()
	birthdate = date(int(Yearentry.get()),int(Monthentry.get()),int(Dayentry.get()))
	age = today.year - birthdate.year - ((today.month,today.day) < (birthdate.month,birthdate.day))
	Label(text=f"{Namevalue.get()} your age is {age}").grid(row=6,column=1)

Label(text = "Name").grid(row = 1,column= 0,padx=90)
Label(text="Year").grid(row=2,column=0)
Label(text="Month").grid(row=3,column=0)
Label(text="Day").grid(row=4,column=0)

Namevalue = StringVar()
Yearvalue = StringVar()
Monthvalue = StringVar()
Dayvalue = StringVar()

Nameentry = Entry(root,textvar =Namevalue)
Yearentry = Entry(root,textvar=Yearvalue)
Monthentry = Entry(root,textvar=Monthvalue)
Dayentry = Entry(root,textvar=Dayvalue)
Nameentry.grid(row=1,column=1,pady=10)
Yearentry.grid(row=2,column=1,pady=10)
Monthentry.grid(row=3,column=1,pady=10)
Dayentry.grid(row=4,column=1,pady=10)
Button(text="Calculate",command=calculateage).grid(row=5,column=1,pady=10)
root.mainloop()