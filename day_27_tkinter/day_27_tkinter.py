from tkinter import *
#the * imports everything

###### creating windows #####
window = Tk()

###### keeping the window on the screen ######

#window.mainloop()
#must be kept at the bottom of the program


######## setting options #########
## During object creation
#fred = Button(self, fg="Red", bg="Blue")

## After object creation (like giving values to keys in dictionaries)
#fred["fg"] = "red"
#fred["bg"] = "blue"

## Using config() method (helps set multiple properties)
# fred.config(fg = "red", bg= "blue")


####### changing title ########
window.title("First GUI programme")


####### changing size of window ######
#minimum size
window.minsize(height=300, width=500)


######## Labels #############
my_label = Label(text = "this is a label", font=("Ariel", 24, "bold"))
###laying out the label/ any other object###
##use .pack()##
    #it will automatically center#
    #you can change the side(left, right, top, bottom)
my_label.pack()
#my_label["text"] = "new text"
## After object creation (like giving values to keys in dictionaries)
    #fred["fg"] = "red"
    #fred["bg"] = "blue"
my_label.config(font=("Ariel", 12))
    ## Using config() method (helps set multiple properties)
    # fred.config(fg = "red", bg= "blue")

######### Buttons #########

def button_click():
    #my_label["text"] = "Button got clicked"
    my_label["text"] = input.get()
### there is a keyword called command where you add a function

button = Button(text="press me", command=button_click)
button.pack()


######## Entry ###########
# entry is basically input
input = Entry()
input["width"] = 10
input.pack()
input.get()


########## More Useful Widgets UwU #############


#######Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()
# END is juat the index


########Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#########Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


##########Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar() ####this is a Class()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


########Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()####this is a Class()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


##########Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()



