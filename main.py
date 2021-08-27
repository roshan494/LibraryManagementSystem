from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from Book import *
from IssueReturn import *
from Student import *
# Add your own database name and password here to reflect in the code
mypass = "850222Ass"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

same=True
n=0.25

# Adding a background image
background_image =Image.open("l.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else: 
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(770,370,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="LIBRARY MANAGEMENT SYSTEM", bg='black', fg='white', font=('Courier',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="BOOK DETAILS",bg='black', fg='white', font=('sans-serif', 15), command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="ISSUE & RETURN",bg='black', fg='white', font=('sans-serif', 15), command=issueBook)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)


btn3 = Button(root,text="STUDENT DETAILS",bg='black', fg='white', font=('sans-serif', 15), command=studentb)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)



root.mainloop()
