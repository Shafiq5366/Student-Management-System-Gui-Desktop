from tkinter import *
import  time
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import  pymysql
root =Tk()# Initialize TK module for our variable root.
root.title("Student Management System")
root.configure(bg='burlywood1')# background color
root.geometry('1174x700+200+50')#fix geometry at a particular position, 200 from x, 50 from y
root.iconbitmap('icon.ico')#title icon
root.resizable(FALSE,FALSE)#Length width both blocked
#=================================================== connectivity

def connectdb():
    def submitdb():
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        # print(host,user,password)


    dbroot=Toplevel()
    dbroot.geometry("470x250+800+230")
    dbroot.grab_set()   # Pehly is window py kam kro tab kahin ur click hoga....mean k ab yeh active window hy only
    dbroot.resizable(FALSE,FALSE)
    dbroot.iconbitmap('icon.ico')
    dbroot.config(bg='steelblue1')
    #labels
    hostlabel=Label(dbroot,text='Enter Host:',bg='burlywood',font=("times", 20 ,'bold'),width=13,anchor="w",relief=GROOVE,borderwidth=3)
    hostlabel.place(x=10,y=10)
    userlabel = Label(dbroot, text='Enter Username:', bg='burlywood', font=("times", 20, 'bold'), width=13, anchor="w",relief=GROOVE,borderwidth=3)
    userlabel.place(x=10, y=70)
    pwlabel = Label(dbroot, text='Enter Password:', bg='burlywood', font=("times", 20, 'bold'), width=13, anchor="w",relief=GROOVE,borderwidth=3)
    pwlabel.place(x=10, y=130)
    #-----------------Entry
    hostval=StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)
    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)
    #submit
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='blue',fg="white",bd=5,width=20,
                        activebackground='white',activeforeground='black',command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

###################################################### dashboard button functions

def addstudent():
    def submitadd():
        print("added")


    addroot=Toplevel(master=dataentryframe)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title("Student Management System")
    addroot.iconbitmap('icon.ico')
    addroot.config(bg='indian red')
    addroot.resizable(FALSE,FALSE)
    #-----------------
    idlabl=Label(addroot,text='Roll No.',bg='burlywood1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabl.place(x=10,y=10)

    namelabl = Label(addroot, text='Enter Name:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    namelabl.place(x=10, y=70)

    mobilelabl = Label(addroot, text='Enter Mobile:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    mobilelabl.place(x=10, y=130)

    emaillabl = Label(addroot, text='Enter Email:.', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    emaillabl.place(x=10, y=190)

    addresslabl = Label(addroot, text='Enter Address:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    addresslabl.place(x=10, y=250)

    genderlabl = Label(addroot, text='Enter Gender:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    genderlabl.place(x=10, y=310)

    doblabl = Label(addroot, text='Enter D.O.B', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    doblabl.place(x=10, y=370)

    #----------------------------- Entry boxes
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderleval = StringVar()
    dobleval = StringVar()


    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderleval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobleval)
    dobentry.place(x=250, y=370)

    submitbutton = Button(addroot, text='Submit', font=('roman', 15, 'bold'), bg='mistyrose3', fg="black", bd=5, width=20,
                          activebackground='white', activeforeground='black',command=submitadd)
    submitbutton.place(x=150, y=420)


    addroot.mainloop()

def searchstudent():
    def search():
        print("search")


    searchroot=Toplevel(master=dataentryframe)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title("Student Management System")
    searchroot.iconbitmap('icon.ico')
    searchroot.config(bg='red4')
    searchroot.resizable(FALSE,FALSE)
    #-----------------
    idlabl=Label(searchroot,text='Roll No.',bg='burlywood1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabl.place(x=10,y=10)

    namelabl = Label(searchroot, text='Enter Name:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    namelabl.place(x=10, y=70)

    mobilelabl = Label(searchroot, text='Enter Mobile:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    mobilelabl.place(x=10, y=130)

    emaillabl = Label(searchroot, text='Enter Email:.', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    emaillabl.place(x=10, y=190)

    addresslabl = Label(searchroot, text='Enter Address:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    addresslabl.place(x=10, y=250)

    genderlabl = Label(searchroot, text='Enter Gender:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    genderlabl.place(x=10, y=310)

    doblabl = Label(searchroot, text='Enter D.O.B:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    doblabl.place(x=10, y=370)

    datelabl = Label(searchroot, text='Enter Date:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3,
                    width=12, anchor='w')
    datelabl.place(x=10, y=430)

    #----------------------------- Entry boxes
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderleval = StringVar()
    dobleval = StringVar()
    dateeval = StringVar()


    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderleval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobleval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateeval)
    dateentry.place(x=250, y=430)





    submitbutton = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), bg='mistyrose3', fg="black", bd=5, width=20,
                          activebackground='white', activeforeground='black',command=search)
    submitbutton.place(x=150, y=480)


    searchroot.mainloop()

def deletestudent():
    pass


def updatestudent():
    def update():
        print("update")

    updateroot = Toplevel(master=dataentryframe)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title("Student Management System")
    updateroot.iconbitmap('icon.ico')
    updateroot.config(bg='maroon')
    updateroot.resizable(FALSE, FALSE)
    # -----------------
    idlabl = Label(updateroot, text='Roll No.', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    idlabl.place(x=10, y=10)

    namelabl = Label(updateroot, text='Enter Name:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    namelabl.place(x=10, y=70)

    mobilelabl = Label(updateroot, text='Enter Mobile:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3,
                       width=12, anchor='w')
    mobilelabl.place(x=10, y=130)

    emaillabl = Label(updateroot, text='Enter Email:.', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=12, anchor='w')
    emaillabl.place(x=10, y=190)

    addresslabl = Label(updateroot, text='Enter Address:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3,
                        width=12, anchor='w')
    addresslabl.place(x=10, y=250)

    genderlabl = Label(updateroot, text='Enter Gender:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3,
                       width=12, anchor='w')
    genderlabl.place(x=10, y=310)

    doblabl = Label(updateroot, text='Enter D.O.B:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3,
                    width=12, anchor='w')
    doblabl.place(x=10, y=370)

    datelabl = Label(updateroot, text='Enter Date:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    datelabl.place(x=10, y=430)

    timelabl = Label(updateroot, text='Enter Time:', bg='burlywood1', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=12, anchor='w')
    timelabl.place(x=10, y=490)

    # ----------------------------- Entry boxes
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderleval = StringVar()
    dobleval = StringVar()
    dateeval = StringVar()
    timeeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderleval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobleval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateeval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeeval)
    timeentry.place(x=250, y=490)






    submitbutton = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), bg='mistyrose3', fg="black", bd=5,
                          width=20,
                          activebackground='white', activeforeground='black', command=update)
    submitbutton.place(x=150, y=537)

    updateroot.mainloop()

def showallstudent():
    print("showall")

def exportstudent():
    print("export")

def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do you want to exit?')
    if (res==True):
        root.destroy()

######################################################
#========================================== Frames
dataentryframe=Frame(root,bg='burlywood2',relief=GROOVE,bd=3)
dataentryframe.place(x=10,y=80,width=320,height=600)
frontlabel=Label(dataentryframe,text='________Dashboard________',width=30,font=('Georgia',20,'bold'),bg='burlywood2',anchor='n')
frontlabel.pack(side=TOP,expand=True)#Expand pory x py ho jae ga
addbtn=Button(dataentryframe,text='Add Student',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=addstudent)
addbtn.pack(side=TOP,expand=True)
searchbtn =Button(dataentryframe,text='Search Student',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=searchstudent)
searchbtn.pack(side=TOP,expand=True)
deletebtn=Button(dataentryframe,text='Delete Student',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=deletestudent)
deletebtn.pack(side=TOP,expand=True)
updatebtn=Button(dataentryframe,text='Update Student',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=updatestudent)
updatebtn.pack(side=TOP,expand=True)
showallbtn=Button(dataentryframe,text='Show All',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=showallstudent)
showallbtn.pack(side=TOP,expand=True)
exportbtn=Button(dataentryframe,text='Export data',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=exportstudent)
exportbtn.pack(side=TOP,expand=True)
exitbtn=Button(dataentryframe,text='Exit',width=25,font=('times',20,'bold'),bd=6,bg='yellow2',activebackground='white',relief=RIDGE,command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
#===========================================================================================    show entry frame

showentryframe=Frame(root,bg='burlywood2',relief=GROOVE,bd=3)
showentryframe.place(x=350,y=80,width=816,height=600)
#------------------------------------------------------------------------------------------- data show
style=ttk.Style()
style.configure('Treeview.Heading',font=('Arial',13,'bold'))
style.configure('Treeview',font=('times',12,'bold'))   # Entries ka style


scroll_x=Scrollbar(showentryframe,orient=HORIZONTAL)
scroll_y=Scrollbar(showentryframe,orient=VERTICAL)
studentable=Treeview(showentryframe,columns=('Roll No.','Name','Mobile No.','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,
                     xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studentable.xview)
scroll_y.config(command=studentable.yview)# scrol k sath oper wali headings b chang hon gi....
studentable.heading('Roll No.',text='Roll No.')
studentable.heading('Name',text='Student Name')
studentable.heading('Mobile No.',text='Mobile No.')
studentable.heading('Email',text='Email')
studentable.heading('Address',text='Address')
studentable.heading('Gender',text='Gender')
studentable.heading('D.O.B',text='D.O.B')
studentable.heading('Added Date',text='Added Date')
studentable.heading('Added Time',text='Added Time')
studentable['show']='headings' # s is required
studentable.column('Roll No.',width=100)
studentable.column('Name',width=200)
studentable.column('Mobile No.',width=200)
studentable.column('Email',width=300)
studentable.column('Address',width=200)
studentable.column('Gender',width=100)
studentable.column('D.O.B',width=150)
studentable.column('Added Date',width=150)
studentable.column('Added Time',width=150)
studentable.pack(fill=BOTH,expand=1)


#========================================================================================
toplabel=Label(root,text='Welcome to Student Management System',bg='deepskyblue2',width=35,bd=4,relief=RIDGE,font=("times",25,'bold'))
toplabel.place(x=240,y=5)
#========================================================    Database button
connectbutton=Button(root,bg="seagreen2", text="Connect to Database",width=19,font=("Arial",13,'bold'),borderwidth=5,bd=5,activebackground='white',command=connectdb)
connectbutton.place(x=960,y=11)
#==================================================
root.mainloop()#Dont close auto