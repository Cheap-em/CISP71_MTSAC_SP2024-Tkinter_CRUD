# Import the required libraries
import sqlite3 as psql
from tkinter import *
from PIL import ImageTk, Image

# Start the program
# Define functions here

path = "/home/howard/Documents/Projects/CISP71_MTSAC_SP2024-Tkinter_CRUD/data/"

# Add the addRecord function
def addRecord():
    # connect to the DB via Postgres SQL
    conn = psql.connect(path+"Quizzing.db")
    try:
        c=conn.cursor()
        c.execute("Inserting values (?,?,?)",
                  (fNameEN.get(),lNameEN.get(),uNameEN.get()))
        conn.commit()
        print("Your record has added successfully")
    except:
        print("Bad record")
        conn.rollback()
    conn.close()


# Get the properties
main = Tk()
main.title("Tkinter CRUD Project")
main.geometry("400x400")
main.iconbitmap()

# Create the button(s)
addBT=Button(main, text="Add Record", command=addRecord)

# Create labels
fNameLB=Label(main,text="First Name")
lNameLB=Label(main,text="Last Name")
uNameLB=Label(main,text="User Name")

# Create entries
fNameEN=Entry(main)
lNameEN=Entry(main)
uNameEN=Entry(main)

# Specify the label grids
fNameLB.grid(row=0, column=0)
lNameLB.grid(row=1,column=0)
uNameLB.grid(row=2, column=0)

#Specify the entry grids
fNameEN.grid(row=0, column=1)
lNameEN.grid(row=1, column=1)
uNameEN.grid(row=2, column=1)

# Specify the button grids
addBT.grid(row=4, column=0)

# Call the mainloop
main.mainloop()