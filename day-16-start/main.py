# import module1
# print(module1.var1)

# from turtle import Turtle, Screen
# Jimmy = Turtle()
# print(Jimmy)
# Jimmy.shape("turtle")
# Jimmy.color("coral")
# Jimmy.forward(100)
# my_screen = Screen()
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water","Fire"])
print(table)