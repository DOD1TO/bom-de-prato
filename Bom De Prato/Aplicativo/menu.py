from tkinter import *
import tkinter as tk
from tkinter import messagebox
from list import *
from recipes import *


class MenuScreen():
    def __init__(self):
        self.root = Tk()
        self.window_menu()
        self.window_frame_menu()
        self.widget_frame_menu()
        self.root.mainloop()

    def window_menu(self):
        self.root.title("Bom de Prato")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root["bg"] = "purple"
    
    def window_frame_menu(self):
        self.frame = Frame(self.root, bd=4)

        self.frame.place(relx=0.17, rely=0.10, relwidth=0.65, relheight=0.80)

    def widget_frame_menu(self):
        # Create Label
        self.lb_bom_de_prato = Label(self.frame, text='Bom de Prato', font='impact 40 bold')
        self.lb_bom_de_prato.place(relx=0.20, rely=0.05)

        # Create Button
        self.btn_list = Button(self.frame, text='List', font='arial 20', command= Aplication)
        self.btn_recipes = Button(self.frame, text='Recipes', font='arial 20', command= RecipesScreen)
        self.btn_restaurants = Button(self.frame, text='Restaurants', font='arial 20')
        self.btn_exit = Button(self.frame, text='Exit', font='arial 20', command= self.ExitApp)

        self.btn_list.place(relx=0.38, rely=0.20, relwidth=0.22, relheight=0.15)
        self.btn_recipes.place(relx=0.38, rely=0.40, relwidth=0.22, relheight=0.15)
        self.btn_restaurants.place(relx=0.38, rely=0.60, relwidth=0.30, relheight=0.15)
        self.btn_exit.place(relx=0.38, rely=0.80, relwidth=0.22, relheight=0.15)
    
    def ExitApp(self):
        self.msgbox = tk.messagebox.askquestion("Exit App", "Really Quit?", icon='error')

        if self.msgbox == 'yes':
            self.root.destroy()
