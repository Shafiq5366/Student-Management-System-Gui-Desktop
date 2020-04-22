from tkinter import *
import  time
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import  pymysql
import pandas
root =Tk()# Initialize TK module for our variable root.
root.title("Student Management System")
root.configure(bg='burlywood1')# background color
root.geometry('1174x700+200+50')#fix geometry at a particular position, 200 from x, 50 from y
root.iconbitmap('icon.ico')#title icon
root.resizable(FALSE,FALSE)#Length width both blocked
#=================================================== connectivity

def connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Incorrect,Please try again..')
            return

        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            strr='create table studentdata(roll int, name varchar(30), mobile varchar (15), email varchar(30), address varchar(100), gender varchar(50),dob varchar(50),date varchar(50), time varchar (50))'
            mycursor.execute(strr)
            strr='alter table studentdata modify column roll int not null'
            mycursor.execute(strr)
            strr='alter table studentdata modify column roll int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Created and Connected Successfully..',parent=dbroot)

        except:
            strr= 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database Connected Successfully..', parent=dbroot)
        dbroot.destroy()



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
        roll=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderleval.get()
        dob=dobleval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        # print(addedtime,addeddate)
        try:
            strr= 'insert into studentdata values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(roll,name,mobile,email,address,gender,dob,addedtime,addeddate))
            con.commit()
            res=messagebox.askyesnocancel('Notification','Roll No.{},Name: {} Addedd Successfully....Do you want to clear the form?'.format(roll,name),parent=addroot)
            if (res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderleval.set('')
                dobleval.set('')
        except:
            messagebox.showerror('Notification','Roll No. already exist,Try another Entry',parent=addroot)
        strr='select * from studentdata'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        # print(datas)
        studentable.delete(*studentable.get_children())
        for i in datas:
            vv= [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentable.insert('',END,values=vv)
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
        roll = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderleval.get()
        dob = dobleval.get()
        addeddate = time.strftime("%d/%m/%Y")

        if(roll != ""):
            strr='select *from studentdata where roll=%s'
            mycursor.execute(strr,(roll))
            datas=mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (name != ""):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (mobile != ""):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (email != ""):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (address != ""):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (gender != ""):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (dob != ""):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)
        elif (addeddate != ""):
            strr = 'select *from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studentable.delete(*studentable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentable.insert('', END, values=vv)




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
    cc=studentable.focus() # jis jga click hoga is function ko pata chaly ga
    content=studentable.item(cc)#focus ka content copy ho jae ga
    pp= content['values'][0]
    strr= 'delete from studentdata where roll=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Roll No. {} deleted successfully..'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    # print(datas)
    studentable.delete(*studentable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studentable.insert('', END, values=vv)




def updatestudent():
    def update():
        roll = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderleval.get()
        dob = dobleval.get()
        date = dateeval.get()
        time = timeeval.get()
        strr='update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where roll=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,roll))
        con.commit()
        messagebox.showinfo('Notification', 'Roll No. {} Updated successfully..'.format(roll),parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentable.delete(*studentable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studentable.insert('', END, values=vv)




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
    cc=studentable.focus()
    content=studentable.item(cc)
    pp=content['values']
    if (len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderleval.set(pp[5])
        dobleval.set(pp[6])
        dateeval.set(pp[7])
        timeeval.set(pp[8])
    updateroot.mainloop()

def showallstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentable.delete(*studentable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studentable.insert('', END, values=vv)

def exportstudent():
    ff=filedialog.asksaveasfilename()
    gg=studentable.get_children()
    roll,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studentable.item(i)
        pp=content['values']
        roll.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Roll','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df=pandas.DataFrame(list(zip(roll,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Students Data is Saved {}'.format(paths))
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