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
        c.execute("insert into primary values (?,?,?)",
                  (fNameEN.get(),lNameEN.get(),uNameEN.get() ) )
        conn.commit()
        print("Your record has added successfully")
    except:
        print("Bad record")
        conn.rollback()
    conn.close()

def displayRecord():
    # Display the record
    conn=psql.connect(path+"Quizzing.db")
    try:
        c=conn.cursor()
        c.execute("select *,oid from main")
        records=c.fetchall()
        #as you see the records is a list with tuples inside it
        print(records)
        
        #loop throu results
        print_records=''
        for record in records:
            print_records +=str(record[0])+" "+ str(record[1])+" "+str(record[2])+"\n"
        query_label=Label(main,text=print_records)
        query_label.grid(row=8,column=0,columnspan=2)
        
        #commit changes
        conn.commit()
        #close connection
        conn.close()
                 
    except:
         print("error in operation")
         conn.rollback()
    conn.close()

# Get the properties
main = Tk()
main.title("Tkinter CRUD Project")
main.geometry("400x400")
main.iconbitmap()

# Create the button(s)
addBT=Button(main, text="Add Record", command=addRecord)
displayRecordBT=Button(main, text="Display Record", command=displayRecord)

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
displayRecordBT.grid(row=4, column=1)

# Call the mainloop
main.mainloop()