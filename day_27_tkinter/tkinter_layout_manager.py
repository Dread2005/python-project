from tkinter import *
# if a layout manager is not placed the object will not show in the window
# There are 3 layout managers you need to know of:
#### Pack ####
# pack()
#always starts from the top down
# can change using the side= keyword
# hard to place it in a specific place

#### Place ####
# place(x= , y=)
# used for precise positioning

#### Grid ####
# looks at the program as a grid that can be divided into multiple columns and rows
# you cant use grid with pack

window = Tk()

window.title("First GUI programme")

window.minsize(height=300, width=500)

my_label = Label(text = "this is a label", font=("Ariel", 24, "bold"))

my_label.grid(column=0, row=0)

my_label.config(font=("Ariel", 12))

def button_click():
    my_label["text"] = input.get()

button = Button(text="press me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="new button", command=button_click)
new_button.grid(column=2, row=0)

input = Entry()
input["width"] = 10
input.grid(column=3, row=2)
input.get()



window.mainloop()