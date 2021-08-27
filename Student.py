from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def searchBook():
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)
    y = 0.25
    sea = search1.get()

    Label(labelFrame, text="%-20s%-40s%-30s%-30s%-30s" % ('StudentID', 'Name', 'Year', 'Phone No', 'Department'), bg='black', fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame, text="------------------------------------------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    seaBooks = "select * from students where studentid= " + sea

    try:
        cur.execute(seaBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-30s%-30s%-30s" % (i[0], i[1], i[2], i[3], i[4]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")


def search():
    global search1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    bookTable = 'books'
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="SEARCH STUDENTS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="ENTER STUDENT ID \n TO BE SEARCHED : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    search1 = Entry(labelFrame)
    search1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='white', fg='black', width=10, height=2, command=searchBook)
    SubmitBtn.place(x=300, y=200)


def updatebook():
    sid = stuInfo1.get()
    name = stuInfo2.get()
    dep = stuInfo3.get()
    year = stuInfo4.get()
    phone = stuInfo5.get()
    updateBooks = "update students set studentname='" + name + "', studentyear='" + year + "', phonenumber='" + phone + "', depatment='" + dep + "'where studentid ='" + sid + "'"
    if(sid=="" or name=="" or dep=="" or year==""or phone==""):
        messagebox.showinfo("Error", "Please add the required details")
    else:
        try:
            cur.execute(updateBooks)
            con.commit()
            messagebox.showinfo('Success', "Student updated successfully")
        except:
            messagebox.showinfo("Error", "Can't update data into Database")



def update():
    global stuInfo1, stuInfo2, stuInfo3, stuInfo4, stuInfo5, Canvas1, con, cur, bookTable, root

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="UPDATE STUDENTS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    option = ["CSE", "MECH", "ECE", "EEE", "CIVIL"]
    option2 = ["FIRST YEAR", "SECOND YEAR", "THIRD YEAR", "FINAL YEAR"]

    lb1 = Label(labelFrame, text="Student ID \n TO BE UPDATED: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.1, relheight=0.1)

    stuInfo1 = Entry(labelFrame)
    stuInfo1.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Student Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.25, relheight=0.08)

    stuInfo2 = Entry(labelFrame)
    stuInfo2.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="Department Name ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.40, relheight=0.08)
    stuInfo3 = ttk.Combobox(labelFrame, value=option, width="37")
    stuInfo3.set("---Select Department Name---")
    stuInfo3.place(relx=0.3, rely=0.40)

    lb4 = Label(labelFrame, text="Year:", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.55, relheight=0.08)
    stuInfo4 = ttk.Combobox(labelFrame, value=option2, width="37")
    stuInfo4.set("---Select Year---")
    stuInfo4.place(relx=0.3, rely=0.55)

    lb5 = Label(labelFrame, text="Phone No. : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)
    stuInfo5 = Entry(labelFrame)
    stuInfo5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.08)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=2, command=updatebook)
    SubmitBtnr.place(x=300, y=200)

def deleteBook1():
    d=messagebox.askquestion("Sure?", "Do you want to delete?")
    if d=="yes":
        deleteBook()
    else:
        pass

def deleteBook():
    issueTable="books_issued"
    sid = stuInfo1.get()
    allBid=[]
    extractBid = "select studentid from students"
    cur.execute(extractBid)
    con.commit()
    for i in cur:
        allBid.append(str(i[0]))

    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(str(i[0]))

        if sid in allBid:
            deleteSql = "delete from students where studentid = '" + sid + "'"
            deleteIssue = "delete from " + issueTable + " where studentid = '" + sid + "'"
            try:
                cur.execute(deleteSql)
                con.commit()
                cur.execute(deleteIssue)
                con.commit()
                messagebox.showinfo('Success', "Student Record Deleted Successfully")
            except:
                messagebox.showinfo("Please check Student ID")

        else:
            messagebox.showinfo("Error", "Student ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Student IDs")

def delete():
    global stuInfo1, Canvas1, con, cur, bookTable, root



    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="DELETE STUDENT", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="STUDENT ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    stuInfo1 = Entry(labelFrame)
    stuInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(labelFrame, text="SUBMIT", bg='white', fg='black', width=10, height=2, command=deleteBook1)
    SubmitBtn.place(x=300, y=200)


def View2(offset):
    root=Tk()
    View(offset,root)

def View(offset,root):
    cur.execute("SELECT count(*) as no from students")
    data_row = cur.fetchone()
    no_rec = data_row[0]
    limit = 20

    q = "SELECT * FROM students order by studentid limit  " + str(offset) + "," + str(limit)
    cur.execute(q)
    e = Label(root, width=30, text='STUDENT ID', borderwidth=5, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = Label(root, width=30, text='NAME', borderwidth=5, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = Label(root, width=30, text='YEAR', borderwidth=5, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = Label(root, width=30, text='PHONE NUMBER', borderwidth=5, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = Label(root, width=30, text='DEPARTMENT', borderwidth=5, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    i = 1
    for student in cur:
        for j in range(len(student)):
            e = Entry(root, width=30, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    while (i <= limit):
        for j in range(len(student)):
            e = Entry(root, width=30, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, "")
        i = i + 1
    back = offset - limit
    next = offset + limit
    b1 = Button(root, text='Next >', command=lambda: View(next,root))
    b1.grid(row=21, column=3)
    b2 = Button(root, text='< Previous ', command=lambda: View(back,root))
    b2.grid(row=21, column=1)
    if (int(no_rec) <= next):
        b1["state"] = "disabled"
    else:
        b1["state"] = "active"

    if (back >= 0):
        b2["state"] = "active"
    else:
        b2["state"] = "disabled"

    root.mainloop()


def Add():
    global stuInfo1, stuInfo2, stuInfo3, stuInfo4,stuInfo5, Canvas1, con, cur, bookTable, root

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD STUDENTS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    option=["CSE","MECH","ECE","EEE","CIVIL"]
    option2=["FIRST YEAR","SECOND YEAR","THIRD YEAR","FINAL YEAR"]

    lb1 = Label(labelFrame, text="Student ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)

    stuInfo1 = Entry(labelFrame)
    stuInfo1.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Student Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.25, relheight=0.08)

    stuInfo2 = Entry(labelFrame)
    stuInfo2.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="Department Name ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.40, relheight=0.08)
    stuInfo3 = ttk.Combobox(labelFrame, value=option, width="37")
    stuInfo3.set("---Select Department Name---")
    stuInfo3.place(relx=0.3, rely=0.40)

    lb4 = Label(labelFrame, text="Year:", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.55, relheight=0.08)
    stuInfo4 = ttk.Combobox(labelFrame, value=option2, width="37")
    stuInfo4.set("---Select Year---")
    stuInfo4.place(relx=0.3, rely=0.55)

    lb5 = Label(labelFrame, text="Phone No. : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)
    stuInfo5 = Entry(labelFrame)
    stuInfo5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.08)

    SubmitBtnr = Button(labelFrame, text="OK", bg='white', fg='black', width=10, height=2, command=Addstudent)
    SubmitBtnr.place(x=300, y=200)

def Addstudent():
    sid = stuInfo1.get()
    name = stuInfo2.get()
    dep = stuInfo3.get()
    year= stuInfo4.get()
    phone=stuInfo5.get()

    print(name,sid,dep,year,phone)
    #status = status.lower()

    insertstu = "insert into students values('" + sid + "','" + name + "','" + year + "','" + phone + "','" + dep + "')"
    if(sid.isnumeric()==False):
        messagebox.showinfo("Error","Please check StudentID")
    elif (sid == "" or name == "" or dep == "" or year == "" or phone == ""):
        messagebox.showinfo("Error", "Please add the required details")
    elif (len(phone)!=10):
        messagebox.showinfo("Error","Please check your phonenumber")
    else:
        try:
            cur.execute(insertstu)
            con.commit()
            messagebox.showinfo('Success', "Student added successfully")
        except:
            messagebox.showinfo("Error", "Can't add data into Database")


def studentb():
    global stuInfo1, stuInfo2, stuInfo3, stuInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1000x500")

    mypass = "850222Ass"
    mydatabase = "db"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

    '''mydatabase = "mydatabase"
    con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)''' 
    cur = con.cursor()

    bookTable = "books"
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="STUDENTS", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    # Submit Button
    SubmitBtn = Button(root, text="ADD", bg='white', fg='black', width=10, height=2, command=Add)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn.place(x=20, y=150)

    SubmitBtn1 = Button(root, text="DELETE", bg='white', fg='black', width=10, height=2, command=delete)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=200)

    SubmitBtn1 = Button(root, text="SEARCH", bg='white', fg='black', width=10, height=2, command=search)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=250)

    SubmitBtn1 = Button(root, text="UPDATE", bg='white', fg='black', width=10, height=2, command=update)
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn1.place(x=20, y=300)

    SubmitBtn2 = Button(root, text="VIEW", bg='white', fg='black', width=10, height=2, command=lambda:View2(0))
    # SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    SubmitBtn2.place(x=20, y=350)

    quitBtn = Button(root, text="Quit", bg='white', fg='black', width=10, height=2, command=root.destroy)
    quitBtn.place(x=450, y=430)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.5)

    root.mainloop()
