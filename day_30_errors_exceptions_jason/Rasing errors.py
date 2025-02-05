#### raise lets us raise our own exceptions ####
    ## raise [error]("this is something I made up")
    #raise KeyError("This is my own error")

### when to use raise ####
height = float(input("Height: "))
weight = float(input("Weight: "))

bmi = weight/(height*height)

if height > 3:
    raise ValueError("Cannot be taller than 3 meters")
print(bmi)