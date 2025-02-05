from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
screen = [*range(-290, 290, 1)]
print(screen)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=600, y=random.choice(screen))
            car.setheading(180)
            car.shape("square")
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def car_move(self):
        for cars in self.all_cars:
            newX = cars.xcor() - MOVE_INCREMENT
            cars.goto(y=cars.ycor(), x=newX)
            cars.distance(cars) - 5

    def car_distance(self, obj):
        for cars in self.all_cars:
            cars.distance(obj)

    def speed_up(self):
        self.carspeed += 2



