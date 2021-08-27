from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from datetime import datetime
from time import strftime
#from ReturnBook import *

# Add your own database name and password here to reflect in the code
mypass = "850222Ass"
mydatabase="db"
con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)

'''mydatabase="mydatabase"
con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)'''
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBid = []

def fine():
    bid = bookInfo1.get()
    date_format = "%d/%m/%Y"
    y = strftime("%d/%m/%Y")
    date = "select date from books_issued where bid= " + bid
    cur.execute(date)
    con.commit()
    for i in cur:
        da = i[0]
    a = datetime.strptime(str(da), date_format)
    b = datetime.strptime(str(y), date_format)
    delta = b - a
    d = delta.days
    if d<=30:
        dq=0
    else:
        dq=(d%30)*10
    messagebox.showinfo("Fine", "The Fine Ammount is Rs."+str(dq))

def returnn():
    bid = bookInfo1.get()
    extractBid = "select bid from " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(str(i[0]))

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from " + issueTable + " where bid = '" + bid + "'"

    print(bid in allBid)
    print(status)
    updateStatus = "update " + bookTable + " set status = 'available' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()

def issue():
    Studentid=""
    x = strftime("%d/%m/%Y")
    
    bid = inf1.get()
    studentid = inf2.get()

    bookTable="books"

    #issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    allBid=[]
    
    
    extractBid = "select bid from books"
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(str(i[0]))
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+studentid+"','"+x+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    cur.execute("select studentid from books_issued where bid = '"+bid+"'")
    rows=cur.fetchall()

    for row in rows:
        Studentid=row[0]
    cur.execute("commit")    
    cur.execute("select studentname from students where studentid = '"+Studentid+"'")
    row1=cur.fetchall()
    for row2 in row1:
        Studentname=row2[0]
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued to " +Studentname)
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(studentid)
    
    allBid.clear()


def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.1, rely=0.3)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.3, relwidth=0.62)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=2, command=returnn)
    SubmitBtnr.place(x=250, y=170)

    SubmitBtnr = Button(labelFrame, text="Check Fine", bg='white', fg='black', width=10, height=2, command=fine)
    SubmitBtnr.place(x=500, y=170)


def issue1():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    lb1 = Label(labelFrame, text="BOOK ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="STUDENT ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=2, command=issue)
    SubmitBtnr.place(x=300, y=200)

    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1000x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="ISSUE/RETURN", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    quitBtn = Button(root,text="Quit",bg='white', fg='black', width=10, height=2, command=root.destroy)
    quitBtn.place(x=450, y=430)

    SubmitBtn1 = Button(root, text="ISSUE", bg='white', fg='black', width=10, height=2, command=issue1)
    SubmitBtn1.place(x=20, y=200)

    SubmitBtn1 = Button(root, text="RETURN", bg='white', fg='black', width=10, height=2, command=returnBook)
    SubmitBtn1.place(x=20, y=300)
    
    root.mainloop()