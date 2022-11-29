from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as db

mydb = db.connect(
  host="localhost",
  user="root",
  password='''Your Database Password''',
  database='''Database Name'''
)


myGui = Tk()
myGui.geometry('600x600')
myGui.title('Aptron Bank')
guiFont = font = dict(family='Courier New, monospaced', size=18)
myGui.config(bg='#0C090A')

img=Image.open('1.png')
img=img.resize((190,190))
img=ImageTk.PhotoImage(img)

asa=Label(myGui,image=img)
asa.place(x=200,y=20)

label=Label(myGui,text='The Most Secure Bank  You Have Probably Used',font=('Aparajita',20),height=1,width=10)
label.place(x=10,y=220,height=50,width=580)


def new_account():
  screen1 = Toplevel()
  screen1.title("Encryption")
  screen1.geometry("1000x600")
  screen1.configure(bg="#0C090A")

  def clear():
    custumer_name.delete(0,END)
    a_number.delete(0,END)
    dobs.delete(0, END)
    addr.delete(0, END)
    occupations.delete(0, END)
    contacts.delete(0,END)


  code = StringVar()
  name= Label(screen1, text="Enter Custumer Name:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=10,height=50,width=250)
  custumer_name= Entry(screen1, textvariable=code, font="Robote 15")
  custumer_name.place(x=300, y=10, height=40, width=300)

  acc_number= Label(screen1, text="Enter Account Number:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=80,height=50,width=250)
  code1=StringVar()
  a_number= Entry(screen1, textvariable=code1, font="Robote 15")
  a_number.place(x=300, y=80, height=40, width=500)

  dob= Label(screen1, text="Enter your Date of Birth:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=160,height=50,width=250)
  code2=StringVar()
  dobs= Entry(screen1, textvariable=code2, font="Robote 15")
  dobs.place(x=300, y=160, height=40, width=200)

  address= Label(screen1, text="Enter Your Address:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=240,height=50,width=250)
  code3=StringVar()
  addr= Entry(screen1, textvariable=code3, font="Robote 15")
  addr.place(x=300, y=240, height=40, width=500)

  contact= Label(screen1, text="Enter Contact Number:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=320,height=50,width=250)
  code4=StringVar()
  contacts= Entry(screen1, textvariable=code4, font="Robote 15")
  contacts.place(x=300, y=320, height=40, width=500)


  occupation= Label(screen1, text="Enter your Occupation:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=400,height=50,width=250)
  code5=StringVar()
  occupations= Entry(screen1, textvariable=code5, font="Robote 15")
  occupations.place(x=300, y=400, height=40, width=500)

  def submit():
    name=code.get()
    accno=code1.get()
    dob=code2.get()
    addrs=code3.get()
    contact=code4.get()
    open_bal=code5.get()

    data1 = (name,accno,dob,addrs,contact,open_bal)
    sql1 = ('insert into Account values(%s , %s , %s , %s , %s , %s)')
    data2 = (name, accno, open_bal)
    sql2 = ('insert into Amount values(%s , %s , %s )')
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    messagebox.showinfo('Submit','Your application are submited')
    screen1.destroy()

  submit = Button(screen1, text="Submit",command=submit, height=2, width=20, font=guiFont,bg='#BDEDFF').place(x=660,y=540,height=40,width=100)
  clear = Button(screen1, text="Clear All",command=clear,  height=2, width=20, font=guiFont,bg='#BDEDFF').place(x=780,y=540,height=40,width=210)


def deposit():
  screen2 = Toplevel()
  screen2.title("Encryption")
  screen2.geometry("800x300")
  screen2.configure(bg="#0C090A")

  code7=StringVar()
  name=Label(screen2,text="Enter amount:", font=guiFont, bg='#82CAFF',height='2',width='25').place(x=10, y=10,height=50,width=250)
  names = Entry(screen2, textvariable=code7, font="Robote 20")
  names.place(x=300, y=10, height=40, width=400)

  acc_number=Label(screen2,text="Account Number:",font=guiFont,bg='#82CAFF',height='2',width='25').place(x=10,y=75,height=50,width=250)
  code8 = StringVar()
  acc_no = Entry(screen2, textvariable=code8, font="Robote 20")
  acc_no.place(x=300, y=75, height=40, width=400)

  def clear():
      acc_no.delete(0,END)
      names.delete(0,END)


  def submit():
    amount =code7.get()
    acc = code8.get()
    a = ('select Balance from Amount where Account_Number=%s')
    data = (acc,)

    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] + int(amount)
    sql = ('update Amount set Balance=%s where Account_Number=%s')
    d = (t, acc)
    x.execute(sql, d)
    x.execute('select * from amount')
    res = x.fetchall()

    mydb.commit()
    messagebox.showinfo('Successfull','Your money is credit')
    screen2.destroy()

  submit = Button(screen2, text="Submit",command=submit, height=2, width=20, font=guiFont,bg='#BDEDFF').place(x=460,y=250,height=40,width=100)
  clear = Button(screen2, text="Clear All",command=clear,  height=2, width=20, font=guiFont,bg='#BDEDFF').place(x=580,y=250,height=40,width=210)

def withdraw():
  screen3 = Toplevel()
  screen3.title("Encryption")
  screen3.geometry("800x300")
  screen3.configure(bg="#0C090A")

  code7 = StringVar()
  name = Label(screen3, text="Enter amount:", font=guiFont, bg='#82CAFF', height='2', width='25').place(x=10, y=10,height=50,width=250)
  names = Entry(screen3, textvariable=code7, font="Robote 20")
  names.place(x=300, y=10, height=40, width=400)

  acc_number = Label(screen3, text="Account Number:", font=guiFont, bg='#82CAFF', height='2', width='25').place(x=10,y=75,height=50,width=250)
  code8 = StringVar()
  acc_no = Entry(screen3, textvariable=code8, font="Robote 20")
  acc_no.place(x=300, y=75, height=40, width=400)

  def clear():
    acc_no.delete(0, END)
    names.delete(0, END)

  def submit():
    amount = code7.get()
    acc = code8.get()
    a = ('select Balance from Amount where Account_Number=%s')
    data = (acc,)

    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - int(amount)
    sql = ('update Amount set Balance=%s where Account_Number=%s')
    d = (t, acc)
    x.execute(sql, d)
    x.execute('select * from amount')
    res = x.fetchall()

    mydb.commit()
    messagebox.showinfo('Successfull', 'Your money is debited')
    screen3.destroy()

  submit = Button(screen3, text="Submit", command=submit, height=2, width=20, font=guiFont, bg='#BDEDFF').place(x=460,y=250,height=40,width=100)
  clear = Button(screen3, text="Clear All", command=clear, height=2, width=20, font=guiFont, bg='#BDEDFF').place(x=580,y=250,height=40,width=210)

def close():
  screen4 = Toplevel()
  screen4.title("Encryption")
  screen4.geometry("800x300")
  screen4.configure(bg="#0C090A")

  acc_number = Label(screen4, text="Account Number:", font=guiFont, bg='#82CAFF', height='2', width='25').place(x=10,y=75,height=50,width=250)
  code8 = StringVar()
  acc_no = Entry(screen4, textvariable=code8, font="Robote 20")
  acc_no.place(x=300, y=75, height=40, width=400)

  def submit():
    acc=code8.get()
    a = ('select Balance from Amount where Account_Number=%s')
    data = (acc,)

    x = mydb.cursor()
    x.execute(a, data)

  submit = Button(screen4, text="Submit", command=submit, height=2, width=20, font=guiFont, bg='#BDEDFF').place(x=460,y=250,height=40,width=100)


new_account = Button(myGui, text="Open new account",command=new_account,  height=2, width=25, font=guiFont,bg='#BDEDFF').place(x=10,y=310,height=60,width=200)
deposit_amount = Button(myGui, text="Deposit Amount",command=deposit,  height=2, width=25, font=guiFont,bg='#BDEDFF').place(x=280,y=310,height=60,width=200)
withdraw_amount=Button(myGui,text='Withdraw Amount',command=withdraw, height=2,width=25, font=guiFont,bg='#BDEDFF').place(x=10,y=410,height=60,width=200)
close_account=Button(myGui,text='Close Account',command=close,height=2,width=25,font=guiFont,bg='#BDEDFF').place(x=280,y=410,height=60,width=200)



myGui.mainloop()