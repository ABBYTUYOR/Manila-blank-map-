from turtle import Turtle, Screen
from manila import Manila
import pandas

screen = Screen()
image = "map_of_manila.png"
screen.title("CITY OF MANILA")
screen.bgpic(image)

data = pandas.read_csv("manila_data.csv")
all_city = data.City.to_list()

manila = Manila()

count = 0

while all_city != len(all_city):

    answer_city = screen.textinput(title=f"{count}/18 City", prompt="What's the other cities?").title()

    if answer_city in all_city:
        count += 1
        manila.show_guess(data, answer_city)



screen.exitonclick()