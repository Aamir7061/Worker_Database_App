from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'aamir' and passwordEntry.get() == '111':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import stu


    else:
        messagebox.showerror('Error', 'Please enter correct credentials')


window = Tk()

window.geometry('1340x700+0+0')
window.title('login Worker Finder')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='grey')
loginFrame.place(x=450, y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
usernameLabel = Label(loginFrame,text='Username',compound=LEFT
                      , font=('times new roman',20, 'bold'), bg='white')

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='black')
usernameEntry.grid(row=1, column=1, pady=10, padx=10)

passwordLabel = Label(loginFrame,text='Password', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='white')

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='black')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15
                     , fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                     activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()