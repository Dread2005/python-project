        #### day 17 Creating custom classes ####

        ##### creating a class: 
         #class {name}car: 

        #naming a class needs every first letter capitalised(PascalCase)

        ###pass###: this keyword passes to the next line

        #### creating Attributes to a class ####:

        #user_1.name = "dread"
        #it is the "." followed by the name(dread) followed by assigning it to 001 that creats the attribute id
        #user_1.id = "001"

        ### Constructor(also known as initialise) ###

        #this is used to specify what should happen when an object is being constructed
        #we do this by using the speciaal __init__ function:

        #class Car:
        #   def __init__ (self{self is the object}):  ### (this __init__ function is used to initialise attributes) ###

        # class Car:
        #   def __init__ (self, seats): ### "seats" is a parameter that you can add to your code ###

        #### creating methods ###

        #class Car:
        #   def enter_race_mode():
        #       self.seats = 2

        # to get the method:
        #{object}my_car.{method}enter_race_mode()


       

class User:
    def __init__(self,user_id,user_name):
        
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0
    
    def follow(self,user):
        user.follower += 1
        self.following += 1
    
        # every time the User class is called you will need to supply the name and id
        #self.follower = 0 is a default(this is how you creat defaults in classes)
   


user_1 = User("001","dread")
user_2 = User("002","jane")

user_1.follow(user_2)

print(user_1.following)
print(user_1.follower)
print(user_2.following)
print(user_2.follower)





        



