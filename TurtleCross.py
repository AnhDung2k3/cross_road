from turtle import Turtle, Screen
import random
import time

colours = ["red", "green", "blue", "yellow", "white", "purple"]

class TurtleCross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.start_cross()
        self.setheading(90)
    
    def turtle_up(self):
        y_pos = self.ycor() + 10
        self.goto(self.xcor(), y_pos)
    
    def turtle_down(self):
        y_pos = self.ycor() - 10
        self.goto(self.xcor(), y_pos)
    
    def cross_success(self):
        if self.ycor() > 260:
            return True
        else:
            return False
    
    def start_cross(self):
        self.goto(0, -260)

class Vehicle(Turtle):
    def __init__(self):
        super().__init__()
        self.vehicle_list = []
        self.vehicle_speed = 3
    
    def rand_vehicle(self):
        random_cycle = random.randint(1, 6)
        if random_cycle == 5:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(colours))
            y_pos = random.randint(-220, 220)
            car.goto(260, y_pos)
            self.vehicle_list.append(car)
    
    def move_vehicle(self):
        for vehicle in self.vehicle_list:
            vehicle.backward(self.vehicle_speed)
    
    def increment_speed(self):
        self.vehicle_speed += 3

class ScorePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        #hide the object, here is turtle
        self.hideturtle()
        self.goto(-240, 255)
        #write a text on screen
        self.write(f"Level: {self.level}", align = "left", font = ("Arial", 30, "normal"))
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = ("Arial", 30, "normal"))
    
    def increment_level(self):
        self.level += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0.0)
        self.write("Game over", align = "center", font = ("Arial", 30, "normal"))

display = Screen()
display.setup(width = 500, height = 600)
display.bgcolor("black")
display.title("Turtle Crosses Road")
#delete the road that turtle goes when begins the game
display.tracer(0)

turtle_cross = TurtleCross()
vehicle = Vehicle()
score_player = ScorePlayer()

display.listen()
display.onkey(turtle_cross.turtle_up, "Up")
display.onkey(turtle_cross.turtle_down, "Down")

start_cross = True

while start_cross:
    time.sleep(0.1)
    display.update()
    vehicle.rand_vehicle()
    vehicle.move_vehicle()
    
    #detect if turtle has contact with the vehicles
    for car in vehicle.vehicle_list:
        if car.distance(turtle_cross) < 20:
            start_cross = False
            score_player.game_over()
    
    #when turtle crosses the road successful
    if turtle_cross.cross_success() == True:
        turtle_cross.start_cross()
        vehicle.increment_speed()
        score_player.increment_level()

display.exitonclick()