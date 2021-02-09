from tkinter import *
from tkinter import ttk
import sqlite3


class Funcs():
    def clear_product(self):
        self.code_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.product_entry.delete(0, END)

    def connect_db(self):
        self.conn = sqlite3.connect("products.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close()

    def create_db(self):
        self.connect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                cod INTEGER PRIMARY KEY,
                product CHAR(40) NOT NULL,
                quantity INTEGER(20)
            );
        """)
        self.conn.commit()
        self.disconnect_db()

    def variables(self):
        self.code = self.code_entry.get()
        self.product = self.product_entry.get()
        self.quantity = self.quantity_entry.get()

    def add_product(self):
        self.variables()
        self.connect_db()

        self.cursor.execute(""" INSERT INTO products (product, quantity)
            VALUES (?, ?) """, (self.product, self.quantity))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        self.clear_product()

    def select_list(self):
        self.listProQuant.delete(*self.listProQuant.get_children())
        self.connect_db()

        roster = self.cursor.execute(""" SELECT cod, product, quantity FROM products ORDER BY product ASC; """)

        for i in roster:
            self.listProQuant.insert("", END, values=i)
        self.disconnect_db()

    def OnDoubleClick(self, event):
        self.clear_product()
        self.listProQuant.selection()

        for n in self.listProQuant.selection():
            col1, col2, col3 = self.listProQuant.item(n, 'values')
            self.code_entry.insert(END, col1)
            self.product_entry.insert(END, col2)
            self.quantity_entry.insert(END, col3)

    def delete_product(self):
        self.variables()
        self.connect_db()
        self.cursor.execute(""" DELETE FROM products WHERE cod = ? """, (self.code))
        self.conn.commit()
        self.disconnect_db()
        self.clear_product()
        self.select_list()

    def edit_product(self):
        self.variables()
        self.connect_db()
        self.cursor.execute(""" UPDATE products SET product = ?, quantity = ? WHERE cod = ?""", (self.product, self.quantity, self.code))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        self.clear_product()


class Aplication(Funcs):
    def __init__(self):
        self.root = Tk()
        self.window()
        self.window_frame()
        self.widget_frame1()
        self.widget_frame2()
        self.clear_product()
        self.create_db()
        self.add_product()
        self.root.mainloop()

    def window(self):
        self.root.title("Supermarket List")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root["bg"] = "blue"

    def window_frame(self):
        self.frame1 = Frame(self.root, bd=4)
        self.frame2 = Frame(self.root, bd=4)

        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widget_frame1(self):
        self.btn1 = Button(self.frame1, text="Save", command=self.add_product)
        self.btn2 = Button(self.frame1, text="Edit", command= self.edit_product)
        self.btn3 = Button(self.frame1, text="Remove", command=self.delete_product)
        self.btn4 = Button(self.frame1, text="Clean", command=self.clear_product)

        self.btn1.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn2.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn3.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn4.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Create Label
        self.lb_code = Label(self.frame1, text="Code")
        self.lb_product = Label(self.frame1, text="Product")
        self.lb_quantity = Label(self.frame1, text="Quantity")

        self.code_entry = Entry(self.frame1)
        self.product_entry = Entry(self.frame1)
        self.quantity_entry = Entry(self.frame1)

        self.lb_code.place(relx=0.05, rely=0.05)
        self.lb_product.place(relx=0.05, rely=0.35)
        self.lb_quantity.place(relx=0.05, rely=0.6)
        self.code_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        self.product_entry.place(relx=0.05, rely=0.45, relwidth=0.08)
        self.quantity_entry.place(relx=0.05, rely=0.7, relwidth=0.08)

    def widget_frame2(self):
        self.listProQuant = ttk.Treeview(self.frame2, height=3, column=("col1", "col2", "col3"))

        self.listProQuant.heading("#0", text="")
        self.listProQuant.heading("#1", text="Code")
        self.listProQuant.heading("#2", text="Product")
        self.listProQuant.heading("#3", text="Quantity")

        self.listProQuant.column("#0", width=1)
        self.listProQuant.column("#1", width=50)
        self.listProQuant.column("#2", width=200)
        self.listProQuant.column("#3", width=125)

        self.listProQuant.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scroll = Scrollbar(self.frame2, orient="vertical")
        self.listProQuant.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listProQuant.bind("<Double-1>", self.OnDoubleClick)
