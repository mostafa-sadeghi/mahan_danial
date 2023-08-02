import turtle

window = turtle.Screen()
window.title("hello")
window.bgcolor('orange')
# window.bgpic("flappyBackground.png")


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

# my_turtle.forward(150)
# my_turtle.left(120)
# my_turtle.forward(150)
# my_turtle.left(120)
# my_turtle.forward(150)
# my_turtle.left(120)

# TODO

"""
تمرین:
کشیدن مربع،
 پنجضلعی
شش ضلعی
هفت  ضلعی
هشت ضلعی
نه ضلعی

"""
sides = int(window.textinput("myshape","How many sides?"))

for i in range(sides):
    my_turtle.forward(100)
    my_turtle.left(360/sides)


turtle.done()
