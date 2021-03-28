from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------- Create Window --------
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# -------- Image --------------
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=2)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(4, 12)]
    password_symbols = [random.choice(symbols) for _ in range(2, 4)]
    password_numbers = [random.choice(numbers) for _ in range(2, 4)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    save_website = website_input.get()
    save_email = email_input.get()
    save_password = password_input.get()

    if len(save_website) == 0 or len(save_password) == 0:
        messagebox.showwarning(title="Oops!", message="Don't leave any fields blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {save_email} \nPassword: {save_password}")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{save_website} | {save_email} | {save_password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                email_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
website = Label(text="Website", font=("Arial", 18))
website.grid(row=2, column=1)

website_input = Entry(width=35)
website_input.grid(row=2, column=2, columnspan=2)
website_input.focus()

email = Label(text="Email", font=("Arial", 18))
email.grid(row=3, column=1)

email_input = Entry(width=35)
email_input.insert(0, "cfstumm@yahoo.com")
email_input.grid(row=3, column=2, columnspan=2)

password = Label(text="Password", font=("Arial", 18))
password.grid(row=4, column=1)

password_input = Entry(width=21)
password_input.grid(row=4, column=2, sticky=W)
generate_password = Button(text = "Generate Password", command=generate_password)
generate_password.grid(row=4, column=3)

add_to_spreadsheet = Button(text = "Add", width=36, command=save)
add_to_spreadsheet.grid(row=5, column=2, columnspan=3)

window.mainloop()
