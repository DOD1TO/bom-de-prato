from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from menu import *


class BackEndRegister():
    def __init__(self):
        self.root = Toplevel()
        self.frame = Frame
        self.user_entry = Entry(self.frame)
        self.password_entry = Entry(self.frame, show="*")
        self.email_entry = Entry(self.frame)
        self.check_var = IntVar()
        self.registerBackEnd()
        self.show_hide_psd()

    def registerBackEnd(self):
        with open('users.txt', 'r') as usersfiles:
            users = usersfiles.read().split("\n")

        with open('passwords.txt', 'r') as usersfiles:
            passwords = usersfiles.read().split("\n")

        with open('emails.txt', 'r') as usersfiles:
            emails = usersfiles.read().split("\n")

        user = self.user_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        if user == '' or password == '' or email == '':
            tk.messagebox.showinfo('ERRO', 'PREENCHA TODOS OS CAMPOS.')

        elif user in users or email in emails:
            tk.messagebox.showinfo('Usuario/Email ja Cadastrado', 'Usuario/Email ja Cadastrado.')

        else:
            with open('users.txt', 'a') as usersfiles:
                usersfiles.write(self.user_entry.get())
                usersfiles.write("\n")

            with open('passwords.txt', 'a') as usersfiles:
                usersfiles.write(self.password_entry.get())
                usersfiles.write("\n")

            with open('emails.txt', 'a') as usersfiles:
                usersfiles.write(self.email_entry.get())
                usersfiles.write("\n")

            tk.messagebox.showinfo('Usuario Cadastrado', 'Usuario Cadastrado.')

            self.root.destroy()

    def show_hide_psd(self):
        if self.check_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")


class RegisterScreen(BackEndRegister):
    def __init__(self):
        self.root = Toplevel()
        self.windowRegister()
        self.window_frameRegister()
        self.widget_frameRegister()
        self.root.mainloop()

    def windowRegister(self):
        self.root.title("Bom de Prato")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root["bg"] = "purple"

    def window_frameRegister(self):
        self.frame = Frame(self.root, bd=4)

        self.frame.place(relx=0.17, rely=0.10, relwidth=0.65, relheight=0.80)

    def widget_frameRegister(self):
        # Create Label
        self.lb_register = Label(self.frame, text='Register', font='impact 40 bold')
        self.lb_login = Label(self.frame, text='User', font='arial 20')
        self.lb_password = Label(self.frame, text="Password", font='arial 20')
        self.lb_email = Label(self.frame, text='Email', font='arial 20')

        self.user_entry = Entry(self.frame)
        self.password_entry = Entry(self.frame, show="*")
        self.email_entry = Entry(self.frame)

        self.lb_register.place(relx=0.32, rely=0.05)
        self.lb_login.place(relx=0.41, rely=0.25)
        self.lb_password.place(relx=0.37, rely=0.40)
        self.lb_email.place(relx=0.41, rely=0.55)
        self.user_entry.place(relx=0.24, rely=0.35, relwidth=0.50)
        self.password_entry.place(relx=0.24, rely=0.50, relwidth=0.50)
        self.email_entry.place(relx=0.24, rely=0.65, relwidth=0.50)

        # Create Button
        self.btn_register = Button(self.frame, text='register', font="arial 20", command=self.registerBackEnd)
        self.btn_register.place(relx=0.38, rely=0.75, relwidth=0.22, relheight=0.15)

        # Checkbutton
        self.check_var = IntVar()
        self.check_show_psw = Checkbutton(self.frame, text='👀', variable=self.check_var, onvalue=1, offvalue=0, height=2, width=5, command=self.show_hide_psd)
        self.check_show_psw.place(relx=0.78, rely=0.50, relwidth=0.10, relheight=0.05)

class LoginBackEnd():
    def __init__(self):
        self.root = Toplevel()
        self.frame = Frame
        self.user_entry = Entry(self.frame)
        self.password_entry = Entry(self.frame, show="*")

    def loginBackEnd(self):
        with open('users.txt', 'r') as usersfiles:
            users = usersfiles.read().split("\n")

        with open('passwords.txt', 'r') as usersfiles:
            passwords = usersfiles.read().split("\n")

        user = self.user_entry.get()
        password = self.password_entry.get()

        login = False

        for i in range(len(users)):
            if user == users[i] and password == passwords[i]:
                tk.messagebox.showinfo('Usuario logado', 'Usuario logado.')
                login = True
                self.root.destroy()
                MenuScreen()

        if not login:
            tk.messagebox.showinfo('Usuario incorreto', 'Usuario incorreto.')


class SignInScreen(LoginBackEnd):
    def __init__(self):
        self.root = Tk()
        self.window()
        self.window_frame()
        self.widget_frame()
        self.root.mainloop()

    def window(self):
        self.root.title("Bom de Prato")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root["bg"] = "purple"

    def window_frame(self):
        self.frame = Frame(self.root, bd=4)

        self.frame.place(relx=0.17, rely=0.10, relwidth=0.65, relheight=0.80)

    def widget_frame(self):
        # Create Label
        self.lb_bom_de_prato = Label(self.frame, text='Bom de Prato', font='impact 40 bold')
        self.lb_login = Label(self.frame, text='User', font='arial 20')
        self.lb_password = Label(self.frame, text="Password", font='arial 20')

        self.user_entry = Entry(self.frame)
        self.password_entry = Entry(self.frame, show='*')

        self.lb_bom_de_prato.place(relx=0.20, rely=0.05)
        self.lb_login.place(relx=0.41, rely=0.25)
        self.lb_password.place(relx=0.37, rely=0.40)
        self.user_entry.place(relx=0.24, rely=0.35, relwidth=0.50)
        self.password_entry.place(relx=0.24, rely=0.50, relwidth=0.50)

        # Create Button
        self.btn_login = Button(self.frame, text='Login', font="arial 20", command=self.loginBackEnd)
        self.btn_register = Button(self.frame, text='Register', font='arial 20', command=RegisterScreen)

        self.btn_login.place(relx=0.24, rely=0.60, relwidth=0.22, relheight=0.15)
        self.btn_register.place(relx=0.52, rely=0.60, relwidth=0.22, relheight=0.15)

SignInScreen()