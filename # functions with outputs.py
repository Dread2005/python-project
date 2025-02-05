# functions with outputs 

#def format_name(f_name,l_name):
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#    #return is important its what gives the output in a function
#    return f"{formated_f_name} {formated_l_name}"
#
#format_string = format_name("Dread","Ford")
#output = len("Dread")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didnt input anything bro"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    #return is important its what gives the output in a function
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("what is your name: "), input("what is your last name: ")))
