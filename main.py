# Import the required libraries
import psycopg as psql
from tkinter import *
from PIL import ImageTk, Image

# Start the program
# Define functions here

path = "/home/howard/Documents/Projects/CISP71_MTSAC_SP2024-Tkinter_CRUD/data/"

# Add the addRecord function
def addRecord():
    # connect to the DB via Postgres SQL
    conn = psql.connect(database = "Quizzing", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)
    try:
        c=conn.cursor()
        c.execute("insert the user's contacts values (?,?,?)", 
                  (fNameEN.get(), lNameEN.get(), uNameEN.get()))
        conn.commit()
        print("Your record has added successfully")
    except:
        print("Bad record")
        conn.rollback()
    conn.close()


# Get the properties
main = Tk()
main.title("Tkinter CRUD Project")
main.geometry("800x800")
main.iconbitmap()

# Create labels
fNameLB=Label(main,text="First Name")
lNameLB=Label(main,text="Last Name")
uNameLB=Label(main,text="User Name")

# Create entries
fNameEN=Entry(main)
lNameEN=Entry(main)
uNameEN=Entry(main)