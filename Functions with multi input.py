#function with input
def greet_with_name(name):
    print(f"jello {name}")

#position argument
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
#greet_with("chiedza", "Joburg")

#key arguments
greet_with(name = "Dread", location = "Joburg")
    