from turtle import Turtle

class Manila(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def show_guess(self, data, answer):
        city_data = data[data.City == answer]
        self.goto(city_data.x.item(), city_data.y.item())
        self.write(city_data.City.item(), align="center", font=("Arial", 8, "normal"))

