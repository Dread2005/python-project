class Animal:
    def __init__(self):
        self.eyes = 2
        self.oxygen = True
        self.swim = True

    def breath(self):
        print("inhale, exhale")


class Fish (Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        #adding to the breath function 
        print("doing this under waater")

    def swim(self):
        print("move tail side to side")


fish = Fish
fish.breath()

#this is how ypu inherit from a class: #
# the Fish class is inheriting from the Animal class
#Animal is the super class(the super class is always the class in brackets)
#super().__init__() is what initiates the super class letting anything from the inheritor inherit from the superclass
