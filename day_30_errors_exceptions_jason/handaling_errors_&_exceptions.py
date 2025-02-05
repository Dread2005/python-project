#FileNotFound error:
#with open("file_name.text") as file:
#   file.read()
## this means there is no file with this name

#KeyError error:
#a_dic = {"KEY": "Value"}
#a_value = a_dic["the_key"]
# we do not get the value because the key we provided does not exist

#IndexError error:
#fruit_list = ["banana", "pear", "coconut"]
#fruit = fruit_list[3]
#this error comes because there is no 3 index(lists start at 0)

#TypeError error:
#text = "abc"
#print(text + 2)
# this will give a type error because you are trying to add an int tot a str

####Catching Exceptions####
# the 4 keywords:
# "try" [comes before a block of code that may cause an exceptions]
try:
    file = open("file_name.text")
    a_dic = {"KEY": "Value"}
    print(a_dic["KEY"]) #"the_key")
# "except(error to except)" [if there was an exception then this is the block of code that must be executed]
except FileNotFoundError:
    file = open("file_name.text")
    file.write("something")
except KeyError as error_message: # error_message = (what the issue is) in this case "the_key"
    print(f"the key {error_message} does not exist")
# "else" [if there was no exception then this block of code will be run]
else:
    content = file.read()
    print(content)
# "finally" [do this no matter what]
finally:
    file.close()
    print("the file has closed")

