from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Country and city game")

Entry_country = Entry(root)
Entry_country.place(relx=5,rely=2)

Entry_city = Entry(root)
Entry_city.place(relx=5,rely=4)

country_list = Label(root,text = "")

