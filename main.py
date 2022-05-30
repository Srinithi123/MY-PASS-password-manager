from tkinter import *
from tkinter import messagebox
#imported msg box modules for the popups from tkinter
from random import choice, randint, shuffle
#radint returns an integer no selected  element from the specified range
import pyperclip
#used to copy abd paste clipboard functions

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list) #this is the method in strings used to join the values given in list , tuples
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
#here a func save is created to write the dats inside the enteried to a data.txt
#when the add button is clicked each website, email and psswd combination should be
#on a new line inside the field al the fields need to be cleared afetr the add button is pressed
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
#the entry widget is used to enter the text strings . it allows the user to enter
#one line of etxt in a single font [get - to fetch the current entry text ]

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:  #a is used to append at the end , with is used
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)  #once it is added we need to clear the entries for that
#here we del from the 0th character and to the end entry

#here we r wrinting into our file f string format for writing string
#after that if we take a look in our project folder that is data,txt we can see the
#datas that we formatted

# ---------------------------- UI SETUP ------------------------------- #
#root = tk() then here image create from tkinter is used then the canvas
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()    #for the cursor
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
#using insert frm tk inter to have the field already entered
email_entry.insert(0, "srinithib27@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)#here when the add button is clicked it needs a trigger a function
#so here i used command and call the func save
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()