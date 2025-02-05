########### HINTS #############
#declare the data type for and leave it as blank:
# age: int
# name: str
# old_enough: bool
# year_month_age: float
#then set it later int the program
#the data type must == what you declared
# age = 12
# name = "Dread"
# old_enough = True
# year_month_age: 12.6

#This can also be done in functions

#### Arrows ####
#you can also specify the output of a datatype using arrows
def police_checker(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_checker(12):
    print("You can drive!!!!")
else:
    print("You may not drive!!!")
