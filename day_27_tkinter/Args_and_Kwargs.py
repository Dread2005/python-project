import tkinter
#window = tkinter.Tk()
#window_title = window.title("tkinter wooow")
#window.minsize(width=500, height=300)

#my_label = tkinter.Label(text="this is a Label")
#my_label.pack(side="left")

########################## ADVANCED ARGUMENTS #######################################
########## Arguments With Default Values ############
#def my_function(a=1, b=2, c=3): #these are the default values
    #do this with a
    #then do this with b
    #finally do this with c
    #### now theres no need to add values
#my_function()
# if you want to change a value in the function:
    #my_function(b=4)
# =... means it has a default value


#window.mainloop()

############################### *args: Many Positional Arguments ################################
### the * is why you can have unlimited arguments:
#def add(*args):
    ## you can also use positions
    #print(args[2])
    #summ = 0
    #for n in args:
        #summ += n
    #return summ

## you can also use positions
#the_sum = add(1, 2, 3, 6)

############################### **kwargs: Many Keyworded Arguments ################################
# the ** is why you have unlimited keyword arguments

# basically creates a dictionary using the keywords as keys and the values are what is assigned to those keys

### Function:
# def calculate(n, **kwargs):
    # for key, value in kwargs.items():
     #  print(value)
     #  print(key)
    # n += kwargs["add"]
    # n *= kwargs["multiply"]
    # print(n)
# calculate(2, add=2, multiply=5)

### Class:
class Car:
    def __init__(self, **kwargs):
    # the kwargs are all the optional arguments that you can pass in when initializing a new object
    # instead of using square brackets[] you can use .get("")
    # if you use .get() you will not have to input a value, it will just output "none"
    # whereas with [] you will have to fill it in or the program will crash
        self.make = kwargs["make"]
        self.model = kwargs.get("model")


my_car = Car(make="nissan")
print(my_car.make)


