from tkinter import *
from tkinter import ttk,messagebox
import pymysql

def delete_worker():
    def delete():
        query='delete from worker where worker_id=%s'
        mycursor.execute(query,(worker_idEntry.get()))
        s=worker_idEntry
        workerTable.delete(*workerTable.get_children())
        result=messagebox.askyesno('CONFIRM','Data Deleted successfully')

        query='SELECT * FROM worker where worker_id=s'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        workerTable.delete(*workerTable.get_children())
        for data in fetched_data:
            datalist=list(data)
            workerTable.insert('',END,values=datalist)

    delete_window = Toplevel()
    worker_idLabel = Label(delete_window, text='Worker_ID', font=('patua one', 20, 'bold'))
    worker_idLabel.grid(row=0, column=0, padx=30, pady=15)
    worker_idEntry = Entry(delete_window, font=('black chancery', 15, 'bold'), width=20)
    worker_idEntry.grid(row=0, column=1, pady=15, padx=10)

    delete_workerButton = ttk.Button(delete_window, text='DELETE WORKER', command=delete)
    delete_workerButton.grid(row=7, columnspan=2, pady=15)


def view_worker():
    query='select * from worker'
    mycursor.execute(query)
    workerTable.delete(*workerTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        workerTable.insert('',END,values=data)


def search_worker():
    def search():
        query='select * from worker where occupation=%s or location=%s'
        if occupationEntry.get=='':
            mycursor.execute(query,(locationEntry.get()))
            workerTable.delete(*workerTable.get_children())
            fetched_data=mycursor.fetchall()
            for data in fetched_data:
                workerTable.insert('',END,values=data)
        elif locationEntry.get=='':
            mycursor.execute(query,(occupationEntry.get()))
            workerTable.delete(*workerTable.get_children())
            fetched_data=mycursor.fetchall()
            for data in fetched_data:
                workerTable.insert('',END,values=data)
        else:
            mycursor.execute(query,(occupationEntry.get(),locationEntry.get()))
            workerTable.delete(*workerTable.get_children())
            fetched_data=mycursor.fetchall()
            for data in fetched_data:
                workerTable.insert('',END,values=data)



    search_window = Toplevel()

    occupationLabel = Label(search_window, text='Occupation', font=('patua one', 20, 'bold'))
    occupationLabel.grid(row=2, column=0, padx=30, pady=15)
    occupationEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=20)
    occupationEntry.grid(row=2, column=1, pady=15, padx=10)

    locationLabel = Label(search_window, text='Location', font=('patua one', 20, 'bold'))
    locationLabel.grid(row=5, column=0, padx=30, pady=15)
    locationEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=20)
    locationEntry.grid(row=5, column=1, pady=15, padx=10)

    search_workerButton = ttk.Button(search_window, text='SEARCH WORKER', command=search)
    search_workerButton.grid(row=7, columnspan=2, pady=15)


def add_worker():
    def add_data():
        if worker_idEntry.get()=='':
            messagebox.showerror('error','all fields are required')
        else:
            query='insert into worker values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(worker_idEntry.get(),worker_nameEntry.get(),occupationEntry.get(),salaryEntry.get(),contact_numberEntry.get(),locationEntry.get()))
            con.commit()
            result=messagebox.askyesno('CONFIRM','Data added successfully')
            
            
            if result:
                worker_idEntry.delete(0,END)
                worker_nameEntry.delete(0, END)
                occupationEntry.delete(0, END)
                salaryEntry.delete(0, END)
                contact_numberEntry.delete(0, END)
                locationEntry.delete(0, END)

                query='SELECT * FROM worker ORDER BY worker_id DESC LIMIT 1'
                mycursor.execute(query)
                fetched_data=mycursor.fetchall()
                workerTable.delete(*workerTable.get_children())
                for data in fetched_data:
                    datalist=list(data)
                    workerTable.insert('',END,values=datalist)

    search_window=Toplevel()
    worker_idLabel=Label(search_window,text='Worker_ID',font=('patua one',20,'bold'))
    worker_idLabel.grid(row=0,column=0,padx=30,pady=15)
    worker_idEntry=Entry(search_window,font=('black chancery',15,'bold'),width=24)
    worker_idEntry.grid(row=0,column=1,pady=15,padx=10)

    worker_nameLabel = Label(search_window, text='Worker_NAME', font=('patua one', 20, 'bold'))
    worker_nameLabel.grid(row=1, column=0, padx=30, pady=15)
    worker_nameEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=24)
    worker_nameEntry.grid(row=1, column=1, pady=15, padx=10)

    occupationLabel = Label(search_window, text='Occupation', font=('patua one', 20, 'bold'))
    occupationLabel.grid(row=2, column=0, padx=30, pady=15)
    occupationEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=24)
    occupationEntry.grid(row=2, column=1, pady=15, padx=10)

    salaryLabel = Label(search_window, text='Salary', font=('patua one', 20, 'bold'))
    salaryLabel.grid(row=3, column=0, padx=30, pady=15)
    salaryEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=24)
    salaryEntry.grid(row=3, column=1, pady=15, padx=10)

    contact_numberLabel = Label(search_window, text='Contact_Number', font=('patua one', 20, 'bold'))
    contact_numberLabel.grid(row=4, column=0, padx=30, pady=15)
    contact_numberEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=24)
    contact_numberEntry.grid(row=4, column=1, pady=15, padx=10)

    locationLabel = Label(search_window, text='Location', font=('patua one', 20, 'bold'))
    locationLabel.grid(row=5, column=0, padx=30, pady=15)
    locationEntry = Entry(search_window, font=('black chancery', 15, 'bold'), width=24)
    locationEntry.grid(row=5, column=1, pady=15, padx=10)

    addworkerButton=ttk.Button(search_window,text='ADD WORKER',command=add_data)
    addworkerButton.grid(row=7,columnspan=2,pady=15)


def connect_database():
    def connect():
        global  mycursor,con
        try:
             con=pymysql.connect(host='localhost',user='root',password='')
             mycursor=con.cursor()
             messagebox.showinfo('success', 'Database Connection is successful',parent=connectWindow)
             connectWindow.destroy()
             addworkerButton.config(state=NORMAL)
             searchworkerButton.config(state=NORMAL)

             deleteworkerButton.config(state=NORMAL)
             viewworkerButton.config(state=NORMAL)
        except:
             messagebox.showerror('Error','Invalid Details',parent=connectWindow)
             return
        try:
           query='create database worker'
           mycursor.execute(query)
           query = 'use worker'
           mycursor.execute(query)


           query='create table worker (worker_id int not null primary key,worker_name varchar(20),occupation varchar(15),salary int(10),contact_number int(15),location varchar(15))'
           mycursor.execute(query)

        except:
            query='use worker'
            mycursor.execute(query)
    connectWindow=Toplevel()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')

    hostnameLabel=Label(connectWindow,text='Host Name',font=('monotype corsiva',20,'bold'))
    hostnameLabel.grid(row=0,column=0)

    hostEntry=Entry(connectWindow,font=('black chancery',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('monotype corsiva', 20, 'bold'))
    usernameLabel.grid(row=1, column=0)
    userEntry = Entry(connectWindow, font=('black chancery', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)


    passwordEntry = Label(connectWindow, text='Password', font=('monotype corsiva', 20, 'bold'))
    passwordEntry.grid(row=2, column=0)
    passwordEntry = Entry(connectWindow, font=('black chancery', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,column=0)

root=Tk()



root.geometry('1440x980+60+0')
root.resizable(0,0)
root.title('WORKER DATABASE')



connectButton=Button(root,text='Connect database',command=connect_database)
connectButton.place(x=1080,y=0)

leftFrame=Frame(root,bg='yellow')
leftFrame.place(x=30,y=100,width=140,height=300)

addworkerButton=Button(leftFrame,text='ADD WORKER',state=DISABLED,command=add_worker)
addworkerButton.grid(row=1,column=0,pady=20)

searchworkerButton=Button(leftFrame,text='SEARCH WORKER',command=search_worker)
searchworkerButton.grid(row=2,column=0,pady=20)

deleteworkerButton=Button(leftFrame,text='DELETE WORKER',command=delete_worker)
deleteworkerButton.grid(row=3,column=0,pady=20)


viewworkerButton=Button(leftFrame,text='VIEW WORKER',command=view_worker)
viewworkerButton.grid(row=5,column=0,pady=20)


rightFrame=Frame(root,bg='yellow')
rightFrame.place(x=180,y=100,width=1200,height=800)

headLabel=Label(root,text='WORKER DATABASES',font=('monotype corsiva',28,'bold'))
headLabel.place(x=300,y=30)


workerTable=ttk.Treeview(rightFrame,columns=('worker_id','worker_name','occupation','salary','contact_number','location'))

workerTable.pack(fill=BOTH,expand=1)


workerTable.heading('worker_id',text='WORKER_ID')
workerTable.heading('worker_name',text='WORKER_NAME')
workerTable.heading('occupation',text='OCCUPATION')
workerTable.heading('salary',text='SALARY')
workerTable.heading('contact_number',text='CONTACT_NUMBER')
workerTable.heading('location',text='LOCATION')


workerTable.config(show='headings')

root.mainloop()