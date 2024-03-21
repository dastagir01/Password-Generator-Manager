import tkinter as t
from tkinter import messagebox
import random
import pyperclip
import math

FONT_NAME = "Ariel"
#
# ---------------------------- Checked Box ------------------------------- #

def checked_box():
    counter = 0

    if var1.get()==1:
        counter = counter + 1

    if var2.get()==1:
        counter = counter + 1

    if var3.get()==1:
        counter = counter + 1

    if var4.get()==1:
        counter = counter + 1

    pswd_len = password_len_entry.get()
    if pswd_len == '':
        t.messagebox.showwarning(title="Warning", message="Please enter Password Length.")

    pswd_len = int(pswd_len)

    if pswd_len < 12 or pswd_len > 36:
        t.messagebox.showwarning(title="Warning", message="Please enter Password Length that is greater than or equal 12 or less than or equal to 36.")

    password_list = []

    if var1.get() ==1:
        letters_cap= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num_letters_cap = random.randint(math.ceil(pswd_len/counter), math.ceil(pswd_len/counter))
        for char in range(num_letters_cap):
            password_list.append(random.choice(letters_cap))

    if var2.get() == 1:
        letters_lower= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        num_letters_lower = random.randint(math.ceil(pswd_len/counter), math.ceil(pswd_len/counter))

        for char in range(num_letters_lower):
            password_list.append(random.choice(letters_lower))

    if var3.get() == 1:
        numbers = ['1', '2', '3', '4', '5','6', '7', '8', '9', '0']
        num_numbers = random.randint(math.ceil(pswd_len/counter), math.ceil(pswd_len/counter))

        for char in range(num_numbers):
            password_list.append(random.choice(numbers))

    if var4.get() ==1:
         symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
         num_symbols = random.randint(math.ceil(pswd_len/counter), math.ceil(pswd_len/counter))

         for char in range(num_symbols):
             password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    # Keep the length of password requested
    password_list = password_list[:pswd_len]
    global password
    #convert list to non-list format
    password = "".join(str(x) for x in password_list)
    # below line is commented out, but you can use this to test if it is working accurately
    # print(f"your password is: {password}; length is {len(password)}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    global password
    #delete any input in the password_entry when generate password button is clicked
    password_entry.delete("0","end")

    checked_box()
    password_entry.insert(0, password)

    #automatically copies the text
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # .get will allow us to get the entry information
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    notes = notes_entry.get()

    if website == "" or email == "" or password == "":
        t.messagebox.showwarning(title="Warning", message="Please insert all required fields.")

    else:
        acceptable = t.messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nWebsite: {website}\nEmail:{email} \nPassword: {password} \nNotes: {notes} \n\nIs it ok to save?")
        if acceptable:
            #input (append: "a") the entries into our text file
            with open("password_db.txt", "a") as data_file:
                data_file.write(f"Website: {website}\nEmail:{email} \nPassword: {password} \nNotes: {notes} \n\n\n")

# ---------------------------- UI SETUP ------------------------------- #
window=t.Tk()
window.title("Password Generator/Manager")
window.config(padx=50, pady=50, bg="white")

#website label
website_label = t.Label(text="Website:*", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
website_label.grid(row=1, column=0)

#website entry
website_entry = t.Entry(width=48)
website_entry.grid(column=1,row=1, columnspan=2)


#email/username label
email_username_label = t.Label(text="Email/Username:*", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
email_username_label.grid(column=0, row=2)

#email/username entry
email_username_entry = t.Entry(width=48)
email_username_entry.grid(column=1,row=2, columnspan=2)

#password length label
password_len_label = t.Label(text="Password Length (min.: 12 & max: 32):*", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
password_len_label.grid(column=0, row=5)

#password length entry
password_len_entry = t.Entry(width=38)
password_len_entry.grid(column=1,row=5)

#selection label
selection_label =t.Label(text="Select boxes for the following to be used in your Password:*", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
selection_label.grid(column=0, row=6)

#checkbox A-Z option
var1 = t.IntVar()
c1 = t.Checkbutton(window, text='A-Z',variable=var1, onvalue=1, offvalue=0, bg="white", command=checked_box)
c1.grid(column=1, row=6)

#checkbox a-z option
var2 = t.IntVar()
c2 = t.Checkbutton(window, text='a-z',variable=var2, onvalue=1, offvalue=0, bg="white", command=checked_box)
c2.grid(column=2, row=6)

#checkbox 0-9 option
var3 = t.IntVar()
c3 = t.Checkbutton(window, text='0-9',variable=var3, onvalue=1, offvalue=0, bg="white", command=checked_box)
c3.grid(column=1, row=7)

#checkbox !#@ etc. option
var4 = t.IntVar()
c4 = t.Checkbutton(window, text='Symbols (e.g: !#@)',variable=var4, onvalue=1, offvalue=0, bg="white", command=checked_box)
c4.grid(column=2, row=7)


#notes label
notes_label = t.Label(text="Notes:", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
notes_label.grid(column=0, row=8)

#notes entry
notes_entry = t.Entry(width=38)
notes_entry.grid(column=1,row=8)

#password label
password_label = t.Label(text="Password:*", fg="#2D6F9F", bg="white", font=(FONT_NAME, 12,"bold"))
password_label.grid(column=0, row=9)

#password entry
password_entry = t.Entry(width=38)
password_entry.grid(column=1,row=9)

#generate button
generate_pass = t.Button(text="Generate", bg="#2D6F9F", command=generate_password, fg="white")
generate_pass.grid(column=2, row=9)

#password label
password_label = t.Label(text="* Required Fields", fg="red", bg="white", font=(FONT_NAME, 8,"italic"))
password_label.grid(column=0, row=10)

#add password button
add_button = t.Button(text="Add", width=40, bg="#2D6F9F", command=save, fg="white")
add_button.grid(column=1, row=10, columnspan=2)

canvas = t.Canvas(width=650, height=650, bg="white", highlightthickness=0)

logo_img = t.PhotoImage(file="logo.png")

canvas.create_image(300,300, image=logo_img)
canvas.grid(column=1, row=0)


window.mainloop()