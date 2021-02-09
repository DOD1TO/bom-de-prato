from tkinter import ttk
import tkinter as tk

TipV = ("Healthy", "Vegetarian", 'Vegan', "Fast Food", "Diabetics")

class RecipesScreen():
    def __init__(self):
        self.root = tk.Tk()
        self.window_recipes()
        self.window_frame_recipes()
        self.widget_frame_recipes()
        self.root.mainloop()

    def window_recipes(self):
        self.root.title("Bom de Prato")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def window_frame_recipes(self):
        self.tabs = ttk.Notebook(self.root) # Abas
        self.tabs.place(x = 0, y = 0, width = 800, height = 600)

        # Create Frames
        self.frames = {}
        for catagory in TipV:
            f = tk.Frame(self.tabs)
            self.tabs.add(f, text=catagory)
            self.frames[catagory] = f

        self.frame_add_recipes = tk.Frame(self.tabs)
        self.tabs.add(self.frame_add_recipes, text='Add New Recipe')

    def widget_frame_recipes(self):
        # Create Label
        self.lb_add_new_recipe = tk.Label(self.frame_add_recipes, text='Add New Recipe', font='arial 20')
        self.lb_where = tk.Label(self.frame_add_recipes, text='Where do you like to add this recipe?', font='arial 10')

        self.recipe_entry = tk.Entry(self.frame_add_recipes)

        self.lb_add_new_recipe.place(relx=0.36, rely=0)
        self.lb_where.place(relx=0, rely=0.10)
        self.recipe_entry.place(relx=0, rely=0.20, relwidth=1, relheight= 0.70)

        # Drop Down Button
        self.Tipvar = tk.StringVar(self.frame_add_recipes)
        self.Tipvar.set("Healthy")
        self.popupMenu = tk.OptionMenu(self.frame_add_recipes, self.Tipvar, *TipV)
        self.popupMenu.place(relx= 0.30, rely= 0.10, relwidth= 0.15, relheight= 0.05)

        btn = tk.Button(self.frame_add_recipes, text="Add", command=self.add)
        btn.place(relx= 0.40, rely= 0.95, relwidth= 0.15, relheight= 0.05)

    def add(self):
        selected_frame = self.frames[self.Tipvar.get()]
        lbl = tk.Label(selected_frame, text=self.recipe_entry.get())
        lbl.pack()