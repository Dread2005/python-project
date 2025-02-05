import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# go straight to def password_saver():

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():


    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)
### Lets you Join
    password = "".join(password_list)
    password = str(password)
    #print(f"Your password is: {password}")
    password_textbox.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_saver():
    website = website_textbox.get()
    email = email_username_textbox.get()
    password = password_textbox.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    website_length = len(website)
    password_length = len(password)

    if website_length == 0 or password_length == 0:
        messagebox.showwarning(title="EY YO!",
                               message="May not leave empty \n P_word must be longer than 6 ch \n website must be "
                                       "more than 1 ch")
#### JASON DATA FILES #####
#with open("password_data.json", "w") as data_file:
    # how to write Json data:
        # json.dump(new_dic, data_file, indent=4)
    # how to read Json data:
        # data = json.load(fp=data_file)
        # print(data)
    # updating old data with the new data
        # data.update(new_data)
    else:
        # You can split the process up to read/update and write:
        try:
            with open("password_data.json", "r") as data_file:
                #read old data
                #try:
                data = json.load(fp=data_file)
                #update old data with new data
                #except JSONDecodeError:
                data.update(new_data)
        except FileNotFoundError:
            with open("password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("password_data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)


        finally:
            password_textbox.delete(0, "end")
            website_textbox.delete(0, "end")


def search():
    the_website = website_textbox.get()
    try:
        with open("password_data.json") as website_search:
            website_s = json.load(website_search)
    except FileNotFoundError:
        messagebox.showwarning(title="error", message="no data found")
    else:
        if the_website in website_s:
            email = website_s[the_website]["email"]
            password = website_s[the_website]["password"]
            messagebox.showinfo(title="here is what you are looking for", message=f"{email}\n{password}")
        else:
            messagebox.showwarning(title="Error", message="No website was found")
            website_textbox.delete(0, "end")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")

canvas = Canvas(width=300, height=300)
canvas.create_image(130, 150, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

email_username_label = Label(text="Email/Username")
email_username_label.grid(column=0, row=3)

password_label = Label(text="Password")
password_label.grid(column=0, row=4)
### to use columnspan, you need sticky="nsew"
website_textbox = Entry()
website_textbox.config(width=21)
website_textbox.focus()
website_textbox.grid(column=1, row=2, sticky="nsew")

search_button = Button(text="search", width=7, command=search)
search_button.grid(column=2, row=2)

email_username_textbox = Entry()
email_username_textbox.insert(0, "Tshifhiwachiedzafordjr@gmail.com")
email_username_textbox.config(width=35)
email_username_textbox.grid(column=1, row=3, columnspan=2, sticky="nsew")

password_textbox = Entry()
password_textbox.config(width=21)
password_textbox.grid(column=1, row=4, sticky="nsew")

password_generate_button = Button(text="Generate", command=gen_password)
password_generate_button.grid(column=2, row=4)

add_button = Button(text="Add")
add_button.config(width=36, command=password_saver)
add_button.grid(column=1, row=5, columnspan=2, sticky="nsew")

window.mainloop()
