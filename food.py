from turtle import Turtle

class Food:

    def __init__(self):
        self.create_food()

    def create_food(self):
        food = Turtle("square")
        food.penup()
        food.color("red")

        #needs to be random
        food.goto(-60,-60)





