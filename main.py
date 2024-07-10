from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [(random.choice(letters)) for _ in range(nr_letters)]
    password_symbol = [(random.choice(symbols)) for _ in range(nr_symbols)]
    password_number = [(random.choice(numbers)) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)

    name = "".join(password_list)
    password.insert(0, name)
    pyperclip.copy(name)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def Add_button():
    a = website.get()
    b = username.get()
    c = password.get()
    new_data={
        a:{
            "email":b,
            "password":c,
        }
    }

    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        messagebox.showinfo(title="Oops", message="You left some field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            username.delete(0,END)
            password.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def Search_button():
    web=website.get()
    search_button.config(bg="blue")
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file is found")
    else:
        if web in data:
            email=data[web]["email"]
            pasword=data[web]["password"]
            messagebox.showinfo(title=f" {web}",message=f"The Email :{email} \n The password :{pasword}")
        else:
            messagebox.showinfo(title=f" {web}",message=f"No details for the search {web}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# canvas
canvas = Canvas(width=200, height=200)
my_picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_picture)
canvas.grid(column=1, row=0)

# Labels
website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)
user_text = Label(text="Email/Username:")
user_text.grid(column=0, row=2)
password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Button
add_button = Button(text="Add", width=43, command=Add_button)
add_button.grid(column=1, row=4, columnspan=3)
generate_password = Button(text="Genarate Password", command=password_generate)
generate_password.grid(row=3, column=2)
search_button=Button(text="Search",width=12,command=Search_button)
search_button.grid(column=2,row=1)

# entry
website = Entry(width=33)
website.grid(column=1, row=1)
website.focus()
username = Entry(width=51)
username.grid(column=1, row=2, columnspan=3)
username.insert(0, "Manoj@gmail.com")
password = Entry(width=33)
password.grid(column=1, row=3)


window.mainloop()
